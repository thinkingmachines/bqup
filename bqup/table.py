class Table():

  view_query = ""

  def __init__(self, dataset, bq_table):
    self.dataset = dataset
    self.table_id = bq_table.table_id
    self.table_type = bq_table.table_type
    dataset.tables.append(self)
    self.view_query = None
    if (self.table_type == "VIEW"):
      self.view_query = dataset.project.client.get_table(bq_table.reference).view_query

  def print(self):
    print("\t\t[{}] {} ({} bytes)".format(self.table_type, self.table_id, len(self.view_query)))

  def export(self, dataset_dir):
    table_path = "{}/{}.{}".format(dataset_dir, self.table_id, self.table_type.lower())
    with open(table_path, "w") as f:
      f.write(self.view_query or "")
