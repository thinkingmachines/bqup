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

1. Run `gcloud auth application-default login` to [run with your personal account](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login) (aka run with scissors)
1. Install `bqup` with `python3 setup.py develop`
1. Run `bqup` (see [Usage](#usage))

## Production

1. Make / Choose a Service Account to use with BQ
1. More steps coming soon
