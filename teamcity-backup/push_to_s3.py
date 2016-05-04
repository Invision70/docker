import boto3
import argparse
import glob
import os

parser = argparse.ArgumentParser(description='Push a TeamCity backup to AWS S3')
parser.add_argument('-bucket', required=True, type=str, metavar='teamcity-backup-bucket',
                   help='S3 bucket to store TeamCity backup in')
parser.add_argument('-access-key', required=True, type=str, metavar='awsiamaccesskey',
                   help='Access key for authenticating to AWS S3')
parser.add_argument('-secret-key', required=True, type=str, metavar='awsiamsecretkey',
                   help='Secret key for authenticating to AWS S3')
parser.add_argument('-threshold', required=False, type=int, metavar='7', default=0,
                   help="Delete backups from S3 older than 'threshold' days. 0 means keep forever (default)")
args = parser.parse_args()

if args.threshold > 0:
    # Setup a start date, from which to keep backups on S3
    today = datetime.now(tz=timezone.utc)
    threshold = timedelta(days=args.threshold)
    start_date = today - threshold

s3client = boto3.client(
    's3',
    aws_access_key_id=args.access_key,
    aws_secret_access_key=args.secret_key
)

# Since we mount teamcity data volume from our teamcity-server container,
# we know backups are located in /var/lib/teamcity/backups
backups = glob.glob('/Users/kristian/teamcity/backup/*.zip')
print(backups)
for abspath in backups:
    tail = os.path.split(abspath)[1]
    print("Uploading backup archive %s to S3 bucket: %s" % (tail,args.bucket))
    s3client.upload_file(Filename=abspath,Bucket=args.bucket,Key=tail)

# If enabled, remove all backups older than 'threshold' days
if args.threshold > 0:
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(args.bucket)
    for obj in s3client.list_objects(Bucket=args.bucket):
        obj_details = obj['Contents'][0]
        if obj_details['LastModified'] < start_date:
            print("removing object with key: %s, from bucket: %s" % (obj_details['Key'],args.bucket))
            response = s3client.delete_object(
                Bucket=args.bucket,
                Key=obj_details['Key'])
            print(response)
