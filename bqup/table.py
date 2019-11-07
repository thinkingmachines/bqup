import json
from os import path


class Table:
    """

    Attributes
    ----------
    dataset : bqup.dataset.Dataset
    export_schema : boolean
        Flag whether or not to save schema of tables
    bq_table : bigquery.table.TableListItem
    """
    view_query = ''
    schema = []

    def __init__(self, dataset, export_schema, bq_table):
        self.dataset = dataset
        self.table_id = bq_table.table_id
        print('\t\tLoading table/view {}...'.format(self.table_id))
        self.table_type = bq_table.table_type
        self.export_schema = export_schema
        dataset.tables.append(self)

        # To support multiple versions of google-cloud-bigquery
        ref = bq_table if hasattr(bq_table, 'path') else bq_table.reference

        if self.table_type == 'VIEW':
            table = dataset.project.client.get_table(ref)
            self.view_query = table.view_query
        elif self.table_type == 'TABLE':
            if export_schema:
                table = dataset.project.client.get_table(ref)
                self.schema = list(map(lambda x: x.to_api_repr(), table.schema))
        elif self.table_type == 'EXTERNAL':
            if export_schema:
                table = dataset.project.client.get_table(ref)
                self.schema = list(map(lambda x: x.to_api_repr(), table.schema))
        elif self.table_type == 'MODEL':
            print('\t\t\tMODEL table type detected, ignoring.')
            pass
        else:
            raise ValueError('Unrecognized table type: {}'.format(self.table_type))

    def _get_export_file_extension(self):
        """Get the file extension for the export file of this table.

        Returns
        -------
        str
            The file extension (i.e. "sql")
        """
        if self.table_type == 'VIEW':
            return 'sql'
        else:
            return 'json'

    def _get_export_table_path(self, dataset_dir):
        """Get the export path for this table

        Parameters
        ----------
        dataset_dir : str
            Directory where dataset will be saved

        Returns
        -------
        str
            The export path
        """
        table_file_name = '{}.{}.{}'.format(self.table_id, self.table_type.lower(), self._get_export_file_extension())
        return path.join(dataset_dir, table_file_name)

    def to_file_contents(self):
        """Return file contents

        Returns
        -------
        str
            File contents
        """
        return self.view_query or json.dumps(self.schema)

    def print_info(self):
        """Print information about the table
        """
        print('\t\t[{}] {} ({} bytes)'.format(
            self.table_type, self.table_id, len(self.view_query)))

    def export(self, dataset_dir):
        """Export dataset to specified directory as either an "sql" or "json" file

        Parameters
        ----------
        dataset_dir : str
            Directory where dataset will be saved
        """
        if not self.export_schema and self.table_type != 'VIEW':
            return
        table_path = self._get_export_table_path(dataset_dir)
        with open(table_path, 'w') as f:
            f.write(self.to_file_contents())
