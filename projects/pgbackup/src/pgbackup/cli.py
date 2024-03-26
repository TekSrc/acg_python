from argparse import Action, ArgumentParser

# https://docs.python.org/3/library/argparse.html , well designed module in standard library
# https://docs.python.org/3/library/time.html#time.strftime

# ➜ python -i src/pgbackup/cli.py
# >>> parser = create_parser()
# >>> args = parser.parse_args(['https://some_url', '--driver', 's3', 'bucket_name'])
# >>> args.url
# 'https://some_url'
# >>> args.driver
# 's3'
# >>> args.destination
# 'bucket_name'
# >>> type(args)
# <class 'argparse.Namespace'>
# >>>
# >>> parser.parse_args()
# usage: cli.py [-h] --driver DRIVER DRIVER url
# cli.py: error: the following arguments are required: url, --driver

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination
    
def create_parser():
    parser = ArgumentParser(description="""Back up PostgreSQL databases locally or to AWS S3.""")

    parser.add_argument("url", help="URL of the PostgreSQL database to backup")
    parser.add_argument("--driver", '-d',
                       help="how & where to store backup",
                       nargs=2,
                       metavar=("DRIVER", "DESTINATION"), # print to look proper when reading my package help text
                       action=DriverAction,
                       required=True
                       )
    return parser

# Entire function is basicaly if I was writing this as a script from top to bottom all in here, including things I don't want like imports
def main():
    import boto3
    import time
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url) # gives dump process to read standard out off that
    
    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime('%Y-%m-%dT%H%M', time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        print(f"Backing up{args.destination} in S3 as {file_name})")
        storage.s3(client, dump.stdout, args.destination, file_name)
    else:
        outfile = open(args.destination, 'wb') # needs to be writeable using bytes
        print(f"Backing up locally to {outfile.name})")
        storage.local(dump.stdout, outfile) # transfer contents into the outfile and close both.
