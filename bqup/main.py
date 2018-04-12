"""bqup - backing up your BigQuery non-data

Usage:
  bqup [-p PROJECT_ID] [-d TARGET_DIR] [-fv]

Options:
  -p PROJECT_ID, --project PROJECT_ID  Project ID to load. If unspecified, defaults to current project in configuration.
  -d TARGET_DIR, --dir TARGET_DIR      The target directory where the project will be written. Defaults to current timestamp.
  -f --force                           Overwrite target directory if it exists.
  -v --verbose                         Print a summary of the loaded project.

"""
import os
from datetime import datetime
from docopt import docopt
from bqup.project import Project


def main():

  args = docopt(__doc__)

  target_dir = args['--dir'] or datetime.isoformat(datetime.now())
  force = args['--force']

  if (not force) and os.path.exists(target_dir):
    print("Target directory already exists. Consider running with -f.")
    exit()

  project_id = args['--project']
  print("Loading {}...".format(project_id or "default project"))
  p = Project(project_id or None)

  if args['--verbose']:
    p.print()

  print("Loaded {}.".format(p.project_id))

  print("Exporting {} to {}...".format(p.project_id, target_dir))
  p.export(target_dir, force=force)
  print("Project {} exported to {}.".format(p.project_id, target_dir))

if __name__ == "__main__":
  main()
