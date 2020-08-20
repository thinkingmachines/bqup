import os
from functools import partial
from bqup.table import Table
from bqup.routine import Routine


class Dataset():
    """For storing all datasets and all the corresponding tables of a project.

    Attributes
    ----------
    project : str
        GCP Project containing the dataset

    dataset_id : str
        GCP Dataset ID of the dataset

    tables : list
        list of Tables that are part of the dataset

    routines : list
        list of Routines(Functions and Procedures) that are part of the dataset
    """

    tables = []

    def __init__(self, project, export_schema, include_routines, bq_dataset):
        """ Creates a Datasets class

        Parameters
        ----------
        project : str
            GCP Project ID that contains the dataset

        export_schema : bool
            If True, will save schema of each table

        bq_dataset : bigquery.dataset.DatasetListItem
            From bigquery.Client

        """
        self.project = project
        self.project.datasets.append(self)
        self.dataset_id = bq_dataset.dataset_id
        print(f'\tLoading dataset {self.dataset_id}...')

        # To support multiple version of google-cloud-bigquery
        if hasattr(project.client, 'list_dataset_tables'):
            self.tables = list(
                map(partial(Table, self, export_schema),
                    project.client.list_dataset_tables(bq_dataset)))
        else:

            if include_routines:
                self.routines = list(
                    map(partial(Routine, self),
                        project.client.list_routines(bq_dataset.reference)))
            else:
                self.routines = []

            self.tables = list(
                map(partial(Table, self, export_schema),
                    project.client.list_tables(bq_dataset.reference)))

    def print_info(self):
        """ Print all the tables of a dataset"""

        print(f"\t[DATASET] {self.dataset_id}")
        for t in self.tables:
            t.print_info()
        for r in self.routines:
            r.print_info()

    def export(self, project_dir):
        """Make a directory for dataset and export schema of each table

        Parameters
        ----------
        project_dir : str
            Path to the project directory where schema will be saved

        """
        dataset_dir = f"{project_dir}/{self.dataset_id}"
        os.makedirs(dataset_dir)
        for t in self.tables:
            t.export(dataset_dir)
        for r in self.routines:
            r.export(dataset_dir)
