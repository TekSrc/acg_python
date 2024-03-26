import csv
import json

# json package is powerful
def to_json_file(export_file, users):
  json.dump(users, export_file, indent=4)
  export_file.close()

# little more complex with csv, but not too bad
def to_csv_file(export_file, users):
  export_file.write('name,id,home,shell\n')
  writer = csv.writer(export_file)
  rows = [[user['name'],user['id'],user['home'],user['shell']] for user in users]
  writer.writerows(rows)
  export_file.close()
