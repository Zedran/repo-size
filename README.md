# Repository size

## Introduction

This is a simple script that checks the size of public repositories on Github. Unlike Gitlab, Github does not display repository size on its website and this tool was created to compensate for this difference.

## Usage

This script accepts a single argument, a Github repository address structured as follows:

```
./repo-size.sh [username]/[repo-name]
```

Github API returns the repository size in KB. This tool converts it to the largest unit of memory that allows for an integer representation.

### Example command

```sh
./repo-size.sh Zedran/repo-size
```

# License

This software is available under MIT License.
