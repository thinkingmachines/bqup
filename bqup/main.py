"""
Used for backing up views in BigQuery.
Requires that `bq` be intalled and configured.
"""

from bqup.dataset import Dataset
from bqup.dataset_object import DatasetObject
from bqup.project import Project


def main():
  # Code below is for testing
  p = Project("tm-heartbeat")
  d = Dataset(p, "eda")
  o = DatasetObject(p, d, "matches_office_in_or_out", "VIEW")
  print(o.get_source())


if __name__ == "__main__":
  main()
