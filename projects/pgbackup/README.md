# pgbackup

A CLI for backing up remote PostgreSQL databases locally or to AWS S3.

```
pgbackup posgtres://username@ip:port/db_name --driver local /path/to/file
```

## Usage

Pass in a full database URL, the storage driver, and destination.

S3 Example w/ bucket name:

```
$ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups
```

Local Example w/ local path:

```
$ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups
```

## Installation From Source

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

```
$ pip install --user -e .
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone git@github.com:example/pgbackup`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`

git ignore from `https://github.com/github/gitignore`

Handling arguments and flags:

`https://docs.python.org/3/library/argparse.html`
`https://acloudguru-content-attachment-production.s3-accelerate.amazonaws.com/1606848446436-CHAPTER%2010.1%20Project%20Setup.txt`

## utilizing backup with simple example.txt file:

![S3 bucket with example txt file uploaded through cli](image.png)

## installing pgbackup package for cli usage I created:

![pgbackup package installed](image-1.png)

## testing cli package for local dump functions:

![local dump working](image-2.png)

## Invocation of the S3 cli command of my package works, also S3 picture showing the example SQL file with 1,000 rows:

![AWS S3 backup cli command](image-3.png)

## backup working before setting timestamp:

![AWS S3 PostgreSQL SQL backup working](image-4.png)

## backup to S3 working with timestamp of filename:

![AWS S3 PostgreSQL SQL backup working with filename](image-5.png)

![Shown in S3 bucket](image-6.png)

# use wheel to distribute the package

![uninstalling to then install via the dist wheel file](image-7.png)
