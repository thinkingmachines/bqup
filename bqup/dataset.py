from functools import partial
from bqup.table import Table


class Dataset():

  tables = []

  def __init__(self, project, bq_dataset):
    self.project = project
    self.project.datasets.append(self)
    self.dataset_id = bq_dataset.dataset_id
    self.tables = list(map(partial(Table, self), project.client.list_tables(bq_dataset.reference)))
