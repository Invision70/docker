import requests
from requests.auth import HTTPBasicAuth
import argparse

prefix_helptext = """
Default: nightly_backup.
Prefix for the teamcity backup file.
Will result in something similar to
nightly_backup__20160502_010121.zip
"""
parser = argparse.ArgumentParser(description='Create a TeamCity backup, via its REST API')
parser.add_argument('-base_url', required=True, type=str, metavar='http[s]://teamcity_hostname[:port]',
                   help='Url to TeamCity server, eg. https://teamcity.server.at.shipbeat')
parser.add_argument('-username', required=True, type=str, metavar='username',
                   help='Teamcity username for http authentication')
parser.add_argument('-password', required=True, type=str, metavar='password',
                   help='Teamcity password for http authentication')
parser.add_argument('-prefix',   required=False, type=str, metavar='filename_prefix', default="nightly_backup",
                   help=prefix_helptext)
args = parser.parse_args()

base_uri = 'httpAuth/app/rest/server/backup'
backup_url = '%s/%s?includeConfigs=true&includeDatabase=true&includeBuildLogs=true&fileName=%s' % (args.base_url,base_uri,args.prefix)
api_response = requests.post(
    backup_url, auth=(args.username, args.password)
)

print(api_response)
print(api_response.headers)
print(api_response.text)
