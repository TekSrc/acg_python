import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Path to the export file')
    parser.add_argument('--format', default='json', choices=['json', 'csv'], type=str.lower)
    return parser

# easy to follow main function.
def main():
    import sys
    from hr import export
    from hr import users as u

    args = create_parser().parse_args()
    users = u.fetch_users()

    if args.path:
        file = open(args.path, 'w', newline='')
    else:
        file = sys.stdout

    if args.format == 'json':
        export.to_json_file(file, users)
    elif args.format == 'csv':
        export.to_csv_file(file, users)
