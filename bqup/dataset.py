import os
from functools import partial
from bqup.table import Table


class Dataset():

    tables = []

    def __init__(self, project, export_schema, bq_dataset):
        self.project = project
        self.project.datasets.append(self)
        self.dataset_id = bq_dataset.dataset_id
        print('\tLoading dataset {}...'.format(self.dataset_id))
        self.tables = list(
            map(partial(Table, self, export_schema), project.client.list_dataset_tables(bq_dataset)))

    def print(self):
        print("\t[DATASET] {}".format(self.dataset_id))
        for t in self.tables:
            t.print()

    def export(self, project_dir):
        dataset_dir = "{}/{}".format(project_dir, self.dataset_id)
        os.makedirs(dataset_dir)
        for t in self.tables:
            t.export(dataset_dir)
