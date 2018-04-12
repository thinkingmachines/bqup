"""
Used for backing up views in BigQuery.
"""

from bqup.project import Project


def main():
  if input("Load default project? (y/n)") == "y":
    print("Loading project...")
    p = Project()
    print("Imported {}:".format(p.project_id))
    for d in p.datasets:
      print("\t{}".format(d.dataset_id))
      for t in d.tables:
        print("\t\t[{}] {}".format(t.table_type, t.table_id))
        if t.view_query:
          print(t.view_query)
    if input("Write project to file system? (y/n)") == "y":
      print("I don't know how to do that yet.")

if __name__ == "__main__":
  main()
