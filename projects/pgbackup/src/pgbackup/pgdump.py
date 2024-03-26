import subprocess
import sys

def dump(url):
    try:
      # pipe will act like filelike object that can capture standard output to read out later by accessing the object that Popen instatiates for me and reading off standard attribute
      return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
      print(f"Error running pg_dump: {err}")
      sys.exit(1)



# >>> from pgbackup import pgdump
# >>> dump = pgdump.dump('posgres://demo:securepassword@54.183.14.200:80/sample')
# >>> pg_dump: error: connection to database "posgres://demo:securepassword@54.183.14.200:80/sample" failed: could not connect to server: No such file or directory
# 	Is the server running locally and accepting
# 	connections on Unix domain socket "/tmp/.s.PGSQL.5432"?
# >>> dump = pgdump.dump('postgres://demo:securepassword@54.183.14.200:80/sample')
# >>> f = open('dump.sql', 'w+b
#   File "<stdin>", line 1
#     f = open('dump.sql', 'w+b
#                              ^
# SyntaxError: EOL while scanning string literal
# >>> f = open('dump.sql', 'w+b')
# >>> f.write(dump.stdout.read())
# 56685
# >>> f.close()
      
      # cat dump.sql
