class Table():

  def __init__(self, dataset, bq_table):
    self.dataset = dataset
    self.table_id = bq_table.table_id
    self.table_type = bq_table.table_type
    dataset.tables.append(self)
    self.view_query = None
    if (self.table_type == "VIEW"):
      self.view_query = dataset.project.client.get_table(bq_table.reference).view_query
