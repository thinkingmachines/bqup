# bqup
BigQuery backup scripts

## Dependencies

1. [Python BigQuery Client Library](https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-usage-python)

## Usage

```
Usage:
  bqup [-p PROJECT_ID] [-d TARGET_DIR] [-fv]

Options:
  -p PROJECT_ID, --project PROJECT_ID  Project ID to load. If unspecified, defaults to current project in configuration.
  -d TARGET_DIR, --dir TARGET_DIR      The target directory where the project will be written. Defaults to current timestamp.
  -f --force                           Overwrite target directory if it exists.
  -v --verbose                         Print a summary of the loaded project.
```

## Development

1. Set up `gcloud` to run with your personal account (aka run with scissors)
1. Set up [application-default](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login): `gcloud auth application-default login`
1. Install `bqup` with `pip3 install -e .` (or `python3 setup.py develop`)
1. Run `bqup` (see [Usage](#usage))
\
## Production

1. `ssh` into the Google Instance you want to run `bqup` from.
1. [Authenticate with Service Account](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)
1. Run `gcloud auth application-default login`
1. Install `bqup` by cloning this repo and running `pip3 install --user -e .` inside the repo.
