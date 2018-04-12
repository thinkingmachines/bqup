from google.cloud import bigquery
from functools import partial
from bqup.dataset import Dataset


class Project():

  datasets = []

  def __init__(self, project_id = None):
    self.client = bigquery.Client(project_id)
    self.project_id = self.client.project
    self.datasets = list(map(partial(Dataset, self), self.client.list_datasets()))
