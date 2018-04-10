"""
Used for backing up views in BigQuery.
Requires that `bq` be intalled and configured.
"""

from classes.Project import Project
from classes.Dataset import Dataset
from classes.DatasetObject import DatasetObject

# Code below is for testing
p = Project("tm-heartbeat")
d = Dataset(p, "eda")
o = DatasetObject(p, d, "matches_office_in_or_out", "VIEW")
print(o.get_source())
