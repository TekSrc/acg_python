# local backups & for AWS S3
# "Local" storage driver stores backups on the local filesystem.
# "Amazon S3" storage driver stores backups on AWS S3.

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/upload_fileobj.html

# PYTHONPATH=./src python
# >>> import boto3
# >>> from pgbackup import storage
# >>> client = boto3.client('s3')
# >>> infile = open('example.txt', 'rb')
# >>> storage.s3(client, infile, 'acg-python-db-backups', infile.name)

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)
