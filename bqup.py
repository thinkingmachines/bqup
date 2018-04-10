"""
Used for backing up views in BigQuery.
Requires that `bq` be intalled and configured.
"""

import subprocess

def run(cmd):
  """Runs a shell command and returns the output as a string."""
  return subprocess.check_output(cmd.split(" ")).decode("UTF-8")

def list_projects():
  return map(
    lambda x: x.split()[0],
    run("bq ls -p").split("\n")[2:-1]
  )

def list_datasets(project):
  return run("bq ls --project_id %s"%(project)).split()[2:]

def parse_object(row):
  (name, type) = row.split()
  return (name, type)

def list_objects(project, dataset):
  objects = run("bq ls %s:%s"%(project, dataset)).split("\n")[2:-1]
  return map(parse_object, objects)

def get_view_source(project, dataset, view):
  return run("bq show --view %s:%s.%s"%(project, dataset, view))

def print_if_view(project, dataset, object):
  if (object[1] == "VIEW"):
    print(get_view_source(project, dataset, object[0]))

# for i in list_objects("tm-heartbeat", "eda"):
#   print_if_view("tm-heartbeat", "eda", i)
