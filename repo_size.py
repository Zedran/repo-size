#!/usr/bin/env python3

import requests
import sys

import utils


URL = "https://api.github.com/repos"


if len(sys.argv) < 2:
    print("repository not specified")
    sys.exit(1)

max_name_len = 0
max_num_len  = 0

info = {}
for repo in sys.argv[1:]:
    resp = requests.get(f"{URL}/{repo}")

    if resp.status_code != 200:
        info[repo] = "unreachable"
    else:
        resp = resp.json()
        info[repo] = utils.convert_kb(resp["size"])

    name_len = len(repo)
    if name_len > max_name_len:
        max_name_len = name_len
    
    num_len = len(info[repo])
    if num_len > max_num_len:
        max_num_len = num_len

for k, v in info.items():
    print(f"{k:<{max_name_len}} : {v:>{max_num_len}}")
