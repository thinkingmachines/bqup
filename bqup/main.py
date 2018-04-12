"""
Used for backing up views in BigQuery.
"""

from bqup.project import Project


def main():
  print("Loading default project...")
  p = Project()
  print("Loaded {}".format(p.project_id))
  if input("Print project contents on screen? (y/n)") == "y":
    p.print()
  if input("Forcibly (deleting existing files) write project to file system? (y/n)") == "y":
    output_dir = "test_output"
    p.export(output_dir, force=True)
    print("Project {} exported to {}".format(p.project_id, output_dir))

if __name__ == "__main__":
  main()
