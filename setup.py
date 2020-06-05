from setuptools import setup

with open('README.md', encoding='utf8') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='bqup',
    version='0.0.7',
    description='BigQuery backup scripts',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Thinking Machines Data Science',
    author_email='engineering@thinkingmachin.es',
    url='https://github.com/thinkingmachines/bqup',
    packages=['bqup'],
    install_requires=requirements,
    license='MIT License',
    entry_points={'console_scripts': ['bqup=bqup.main:main']},
    keywords=['google bigquery', 'bigquery', 'bq', 'backup', 'bqup']
)
