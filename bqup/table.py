import json

class Table():

    view_query = ''
    schema = []

    def __init__(self, dataset, export_schema, bq_table):
        self.dataset = dataset
        self.table_id = bq_table.table_id
        print('\t\tLoading table/view {}...'.format(self.table_id))
        self.table_type = bq_table.table_type
        dataset.tables.append(self)

        if (self.table_type == 'VIEW'):
            table = dataset.project.client.get_table(bq_table.reference)
            self.view_query = table.view_query
        elif (self.table_type == 'TABLE'):
            if export_schema:
                table = dataset.project.client.get_table(bq_table.reference)
                self.schema = list(map(lambda x: x.to_api_repr(), table.schema))
        else:
            print('Unrecognized table type: {}'.format(self.table_type))
            exit()


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
