# HR CLI Python Project 2

I've been asked to create a tool to eport a system's user information into formats that can be used by other departments. The xommand will be able to export user names, IDs, home directories, and shells as either JSON or CSV. My command will not incude information about system users. However, by default, the command will display the information as JSON to Stdout, but the `--format` flag will allow a person to specify `csv` as an alternative ezport type. Additionally, a file can be specified by using the `--path` flag.

## Various ways my HR tool can be used:

```
$ hr --format=csv --path=path/to/users.csv
$ hr --path=path/tousers.json

$ hr
[
  {
    "name": "a_cloud_user",
    "id": 1003,
    "home": "/home/a_cloud_user",
    "shell": "/bin/bash"
  },
  {
    "name": "scott",
    "id": 1004,
    "home": "/home/scott",
    "shell": "/bin/zsh"
  },
]

$ hr --format=csv
name,id,home,shell
a_cloud_user,1003,'home/a_cloud_user,/bin/bash
scott,1004,/home/scott,/bin/zsh
```
