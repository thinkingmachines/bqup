import os
import shutil
from google.cloud import bigquery
from functools import partial
from bqup.dataset import Dataset

print('BigQuery version: {}'.format(bigquery.__version__))

class Project():

    datasets = []

    def __init__(self, project_id=None, export_schema=False):
        self.client = bigquery.Client(project_id)
        self.project_id = self.client.project
        print('Loading project {}...'.format(self.project_id))
        self.datasets = list(
            map(partial(Dataset, self, export_schema), self.client.list_datasets()))

    def print(self):
        print("[PROJECT] {}".format(self.project_id))
        for d in self.datasets:
            d.print()

    def export(self, directory, force=False):
        """Exports a project's contents to the given directory in the filesystem."""
        if os.path.exists(directory):
            if force:
                shutil.rmtree(directory)
            else:
                raise Exception(
                    "Cannot extract project contents to an existing directory: [{}]".format(directory))

        project_dir = "{}/{}".format(directory, self.project_id)
        os.makedirs(project_dir)
        for d in self.datasets:
            d.export(project_dir)
