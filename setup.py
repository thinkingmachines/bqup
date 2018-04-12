from setuptools import setup, find_packages


setup(
  name="bqup",
  version="0.0.1",
  packages=find_packages('bqup'),
  entry_points={
    "console_scripts": ["bqup=bqup.main:main"],
  },
  install_requires=["docopt"]
)
