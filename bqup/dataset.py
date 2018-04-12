from bqup.util import run


class Dataset():

  objects = []

  def __init__(self, project, name):
    self.project = project
    self.name = name
    project.datasets.append(self)

  @staticmethod
  def list(project):
    return list(map(
      lambda name: Dataset(project, name),
      run("bq ls --project_id {}".format(project.name)).split()[2:]
    ))
