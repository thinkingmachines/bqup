from bqup.util import run


class Project():

  def __init__(self, name):
    self.name = name
    self.datasets = []

  @staticmethod
  def list():
    return list(map(
      lambda x: Project(x.split()[0]),
      run("bq ls -p").split("\n")[2:-1]
    ))
