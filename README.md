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

## Production

1. `ssh` into the Google Instance you want to run `bqup` from.
1. [Authenticate with Service Account](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)
1. Run `gcloud auth application-default login`
1. Install `bqup` by cloning this repo and running `pip3 install --user -e .` inside the repo.

### Setting up regular backups

1. On the machine that will run your backups, set up your git config (username, email, the usual).
1. Make a directory to use as the Git repository. For this example, let's use `repo`:

    ```
    mkdir repo
    cd repo
    git init
    ```

1. Add the remote to the git repository (ideally a GCP repository). For this example, let's use `google`:

    ```
    git remote add google <url-to-remote-repository>
    ```

1. Create a script called `bqup.sh` that follows the following template. For our example, our repository is dedicated to backups, so we just assume that our `HEAD` is the latest and just push gently to `master`.

    ```
    #!/bin/bash
    <path-to-bqup> -p <project-id> -d <path-to-repo>/projects -fv >> <path-to-log-file>
    cd <path-to-repo>
    git add .
    git commit -m "Automated bqup"
    git push <remote> <branch>
    ```

1. Add this script to your [crontab](https://awc.com.my/uploadnew/5ffbd639c5e6eccea359cb1453a02bed_Setting%20Up%20Cron%20Job%20Using%20crontab.pdf) to run as frequently as your heart desires.
