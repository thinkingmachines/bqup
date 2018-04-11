import subprocess


def run(cmd):
  """Runs a shell command and returns the output as a string."""
  return subprocess.check_output(cmd.split(" ")).decode("UTF-8")
