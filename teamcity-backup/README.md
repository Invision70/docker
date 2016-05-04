This container is intended to play together with [shipbeat/teamcity-server], but may very well work with any TeamCity server container.  
This container takes a backup of TeamCity server, using the REST API, and pushes the archive to S3. In fact it pushes all backup archives to S3 if you happened to do any manual backups via the UI in the meantime.  

There's quite a few environment variables that must be set in order for this to work.
```
    TEAMCITY_BASE_URL "the url pointing to teamcity server"
    TEAMCITY_USERNAME "username for accessing teamcity server via http basic auth"
    TEAMCITY_PASSWORD "password for accessing teamcity server via http basic auth"
    AWS_S3_BUCKET     "S3 bucket to store backup in"
    AWS_ACCESS_KEY    "IAM access key for user permitted to push to AWS_S3_BUCKET"
    AWS_SECRET_KEY    "IAM secret key for user permitted to push to AWS_S3_BUCKET"
    KEEP_DAYS         "Number of days to keep backup archive on S3. 0 means infinite"
```

So, now we can start our backup with this command:
```bash
    docker run --name tcbak --rm=true \
    --volumes-from teamcitysrv \
    -e TEAMCITY_BASE_URL="http://teamcity.server.at.shipbeat" \
    -e TEAMCITY_USERNAME=backupoperator \
    -e TEAMCITY_PASSWORD=secretpass \
    -e AWS_S3_BUCKET=teamcity-backup-bucket \
    -e AWS_ACCESS_KEY=xxxxxxxx \
    -e AWS_SECRET_KEY=xxxxxxxx \
    -e KEEP_DAYS=7 \
     shipbeat/teamcity-backup
```
The container will stop and remove itself as soon as it finishes.
