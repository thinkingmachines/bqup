from bqup.util import run


class Project(object):

  def __init__(self, name):
    self.name = name
    self.datasets = []

  @classmethod
  def list(cls):
    return list(map(
      lambda x: Project(x.split()[0]),
      run("bq ls -p").split("\n")[2:-1]
    ))
