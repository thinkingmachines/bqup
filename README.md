# bqup

bqup is a backup tool for BigQuery projects. It can export a BigQuery
project's structure and source code while mimicking the hierarchy of
datasets and tables.

![How bqup
works](https://thinkingmachin.es/stories/coding-safely-in-the-cloud/solution.png
"How bqup works")

For the full story of why we made bqup, check out our [blog
post](https://stories.thinkingmachin.es/coding-safely-in-the-cloud/)!

## Installation

bqup can be installed using `pip`.

```
$ pip install bqup
```

Alternatively, you can also clone the repository then run `install`.

```
$ git clone https://github.com/thinkingmachines/bqup.git
$ cd bqup
$ python3 setup.py install
```

## Usage

### Command line options

You can list down the options by running `bqup --help`.

```text
bqup [-p PROJECT_ID] [-d TARGET_DIR] [-fvxr] [-e REGEX]

Options:
  -p PROJECT_ID, --project PROJECT_ID  Project ID to load. If unspecified,
                                       defaults to current project in
                                       configuration.
  -d TARGET_DIR, --dir TARGET_DIR      The target directory where the project
                                       will be written. Defaults to current
                                       timestamp.
  -f --force                           Overwrite target directory if it exists.
  -v --verbose                         Print a summary of the loaded project.
  -x --schema                          Export table schemata as json.
  -r --routine                         Include routines in export.
  -e REGEX, --regex REGEX              Regex pattern to filter datasets to be exported.
```

### Development

1. Set up `gcloud` to run with your personal account (aka run with scissors).
2. Set up
   [application-default](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login).

   ```
   $ gcloud auth application-default login
   ```

3. Install `wheel`.

   ```
   $ pip3 install wheel
   ```

4. Install bqup.

   ```
   pip3 install -e .
   ```

   Alternatively, you can also install it using:

   ```
   python3 setup.py develop
   ```

5. Run bqup (see [Usage](#usage)).

### Setting up regular backups

Check out [bqup-starter](https://github.com/thinkingmachines/bqup-starter) to set up regular bqups using GitHub's workflows!

### Distribution

Run `make test` to try a test upload.

Run `make dist` to upload a distribution.

Both of these will call `make build`, which rebuilds the package locally.

## Contributing

If you wish to contribute, check out our [contributing
guide](https://github.com/thinkingmachines/bqup/blob/master/CONTRIBUTING.md)!

A list is maintained for all external contributors who have submitted pull
requests that were subsequently approved. Users are allowed and encouraged to
fork the project and submit pull requests and issues. We only request that
contributions adhere to these guidelines:

- [Commit messages](https://chris.beams.io/posts/git-commit/)
- [Github flow](https://guides.github.com/introduction/flow/)

The official maintainers in charge of responding to issues and merging pull
requests are:

- [Pepe Bawagan](https://github.com/syk0saje)
- [Mark Steve Samson](https://github.com/marksteve)
- [Carlson Cheng](https://github.com/crcheng)

## Contributors

Thanks to all these wonderful people who've helped out with bqup:

<table><tr><td align="center"><a href="https://github.com/jgtiu"><img src="https://avatars1.githubusercontent.com/u/33926951?s=400&v=4" width="100px;" alt="Jess"/><br /><sub><b>Jess</b></sub></a></td><td align="center"><a href="https://github.com/magtanggol03"><img src="https://avatars1.githubusercontent.com/u/25030847?s=400&v=4" width="100px;" alt="Ram"/><br /><sub><b>Ram</b></sub></a></td><td align="center"><a href="https://github.com/pberba"><img src="https://avatars0.githubusercontent.com/u/6505743?s=400&v=4" width="100px;" alt="Pepe Berba"/><br /><sub><b>Pepe Berba</b></sub></a></td><td align="center"><a href="https://github.com/tim-tmds"><img src="https://avatars2.githubusercontent.com/u/50472403?s=400&v=4" width="100px;" alt="Tim Pron"/><br /><sub><b>Tim Pron</b></sub></a></td><td align="center"><a href="https://github.com/enzoampil"><img src="https://avatars2.githubusercontent.com/u/39557688?s=400&v=4" width="100px;" alt="Enzo"/><br /><sub><b>Enzo</b></sub></a><br /></td><td align="center"><a href="https://github.com/ardieorden"><img src="https://avatars1.githubusercontent.com/u/17169362?s=400&v=4" width="100px;" alt="Ardie"/><br /><sub><b>Ardie</b></sub></a><br /></td></tr></table>

- [bhuesemann](https://github.com/bhuesemann)
- [bzieba-spartez](https://github.com/bzieba-spartez)
- [profwacko](https://github.com/profwacko)

## Disclaimers

bqup is maintained on a **best effort** basis:

- No amount of official time is currently being dedicated to the regular
  maintenance of this project.
- Thinking Machines does not make any guarantees about the quality of the
  software.

Thinking Machines reserves the rights to:

- refuse to resolve issues
- close issues without resolution
- request changes to pull requests
- reject pull requests outright
