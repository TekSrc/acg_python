from argparse import Action, ArgumentParser

# https://docs.python.org/3/library/argparse.html , well designed module in standard library

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
    parser.add_argument("--driver",
                       help="how & where to store backup",
                       nargs=2,
                       action=DriverAction,
                       required=True
                       )
    return parser
