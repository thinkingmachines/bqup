from bqup.util import run


class DatasetObject(object):

  def __init__(self, project, dataset, name, type):
    self.project = project
    self.dataset = dataset
    self.name = name
    self.type = type
    dataset.objects.append(self)

  def get_source(self):
    if self.type == "VIEW":
      self.source = run("bq show --view {}:{}.{}".format(
        self.project.name, self.dataset.name, self.name))
      return self.source

  @staticmethod
  def list(project, dataset):
    return list(map(
      lambda x: DatasetObject(project, dataset, *(x.split())),
      run("bq ls {}:{}".format(project.name, dataset.name)).split("\n")[2:-1]
    ))
