# Repository size

## Introduction

This is a simple script that checks the size of public repositories on Github. Unlike Gitlab, Github does not display repository size on its website and this tool was created to compensate for this difference.

## Usage

This script takes any number of repository names structured as follows:

```bash
./repo_size.py [username]/[repo-name] [username]/[repo-name]
```

### Example command

```bash
./repo_size.py Zedran/repo-size torvalds/linux
```

# License

This software is available under MIT License.
