from setuptools import setup, find_packages


setup(
    name="bqup",
    version="0.0.2",
    packages=find_packages('bqup'),
    entry_points={
        "console_scripts": ["bqup=bqup.main:main"],
    },
    install_requires=["docopt", "google-cloud-bigquery==1.1.0"],
    description='BigQuery backup scripts'
)
