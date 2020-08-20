"""bqup - backing up your BigQuery non-data

Usage:
  bqup [-p PROJECT_ID] [-d TARGET_DIR] [-fvxr] [-e REGEX]

Options:
  -p PROJECT_ID, --project PROJECT_ID  Project ID to load. If unspecified, defaults to current project in configuration.
  -d TARGET_DIR, --dir TARGET_DIR      The target directory where the project will be written. Defaults to current timestamp.
  -f --force                           Overwrite target directory if it exists.
  -v --verbose                         Print a summary of the loaded project.
  -x --schema                          Export table schemata as json.
  -r --routine                         Include routines in export.
  -e REGEX, --regex REGEX              Regex pattern to filter datasets to be exported.
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
    print(f"Loading {project_id or 'default project'}...")
    p = Project(project_id or None, args['--schema'], args['--routine'], args['--regex'])

    if args['--verbose']:
        p.print_info()

    print(f"Loaded {p.project_id}.")

    print(f"Exporting {p.project_id} to {target_dir}...")
    p.export(target_dir, force=force)
    print(f"Project {p.project_id} exported to {target_dir}.")


if __name__ == "__main__":
    main()
