import json

class Table():

    view_query = ''
    schema = []

    def __init__(self, dataset, bq_table):
        self.dataset = dataset
        self.table_id = bq_table.table_id
        self.table_type = bq_table.table_type
        dataset.tables.append(self)

        table = dataset.project.client.get_table(bq_table.reference)
        if (self.table_type == 'VIEW'):
            self.view_query = table.view_query
        else:
            self.schema = list(map(lambda x: x.to_api_repr(), table.schema))

    def to_file_contents(self):
        return self.view_query or json.dumps(self.schema)

    def print(self):
        print('\t\t[{}] {} ({} bytes)'.format(
            self.table_type, self.table_id, len(self.view_query)))

    def export(self, dataset_dir):
        table_path = '{}/{}.{}'.format(dataset_dir,
                                       self.table_id, self.table_type.lower())
        with open(table_path, 'w') as f:
            f.write(self.to_file_contents())
