import os
import shutil
from google.cloud import bigquery
from functools import partial
from bqup.dataset import Dataset
import re


class Project():
    """Project that enables content exploration and exporting.

    Parameters
    ----------
    project_id : str
        A unique identifier for your project, composed of the project name and an assigned number.
    export_schema : bool
        If True, will save schema of each table.

    Attributes
    ----------
    client : bigquery.client.Client
        Client to bundle configuration needed for API requests.
    project_id : str
        A unique identifier for the project, composed of the project name and an assigned number.
    datasets : list
        Datasets within the project.
    """

    datasets = []

    def __init__(self, project_id=None, export_schema=False, include_routines=False, regex_pattern=None):
        self.client = bigquery.Client(project_id)
        self.project_id = self.client.project
        self.regex_pattern = regex_pattern

        print(f'Loading project {self.project_id}...')
        self.datasets = list(
            map(partial(Dataset, self, export_schema, include_routines),
                filter(self.matches_regex, self.client.list_datasets())))

    def matches_regex(self, dataset):
        """Returns match if regex pattern exists and is found in dataset_id"""
        return not self.regex_pattern or re.match(self.regex_pattern, dataset.dataset_id)

    def print_info(self):
        """Displays names of datasets, tables, and views as a hierarchical tree."""
        print(f"[PROJECT] {self.project_id}")
        for d in self.datasets:
            d.print_info()

    def export(self, directory, force=False):
        """Exports a project's contents to the given directory in the filesystem.

        Parameters
        ----------
        directory : path-like object
            Directory to which the project's contents will be exported.
        force : bool
            If True and directory exists, will delete the directory and its contents.
        """
        if os.path.exists(directory):
            if force:
                shutil.rmtree(directory)
            else:
                raise Exception(f"Cannot extract project contents to an existing directory: [{directory}]")

        project_dir = f"{directory}/{self.project_id}"
        os.makedirs(project_dir)
        for d in self.datasets:
            d.export(project_dir)
