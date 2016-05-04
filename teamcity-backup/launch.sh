python3 /teamcity_backup.py -base_url $TEAMCITY_BASE_URL -username $TEAMCITY_USERNAME -password $TEAMCITY_PASSWORD
python3 /push_to_s3.py -bucket $AWS_S3_BUCKET -access-key $AWS_ACCESS_KEY -secret-key $AWS_SECRET_KEY -threshold $KEEP_DAYS
rm -f /var/lib/teamcity/backup/*.zip
