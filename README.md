# bqup
BigQuery backup scripts

## Dependencies

1. [Python BigQuery Client Library](https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-usage-python)

## Development

1. Run `gcloud auth application-default login` to [run with your personal account](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login) (aka run with scissors)
1. Install `bqup` with `python3 setup.py develop`
1. Run `bqup` (see Usage instructions in `main.py`)

## Production

1. Make / Choose a Service Account to use with BQ
1. More steps coming soon
