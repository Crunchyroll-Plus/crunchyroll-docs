#!/usr/bin/python

import requests
import re
import base64
import os
import json
import sys

args = sys.argv[1:]

player_bundle = "https://static.crunchyroll.com/vilos-v2/web/vilos/js/bundle.js"

response = requests.get(player_bundle)
if not response.ok:
    raise requests.ConnectionError(f"Couldn't connect to {player_bundle}.")

tokens = re.search(r'prod="([\w-]+:[\w-]+)",\w+\.staging="([\w-]+:[\w-]+)",\w+\.proto0="([\w-]+:[\w-]+)"', response.text)
if not tokens:
    raise ValueError("Couldn't find tokens.")

prod, staging, proto = tokens.groups()

def get_b64(string: str) -> str:
    return base64.b64encode(string.encode("iso-8859-1")).decode()

if __name__ == "__main__":
    prod_user, prod_pass = prod.split(":")
    path = os.path.join(os.path.dirname(__file__), "basic.json")
    prod_token = get_b64(prod)

    if len(args) > 0 and args[0] == "update":
        with open(path, "w") as f:
            staging_user, staging_pass = staging.split(":")
            proto_user, proto_pass = proto.split(":")

                
            f.write(json.dumps({
                "production": {
                    "token": prod_token,
                    "username": prod_user,
                    "password": prod_pass
                },
                "staging": {
                    "token": get_b64(staging),
                    "username": staging_user,
                    "password": staging_pass
                },
                "proto": {
                    "token": get_b64(proto),
                    "username": proto_user,
                    "password": proto_pass
                }
            }, indent=4))

        print(f"Dumped tokens to {path}")
    else:
        print("Basic Auth Token:")
        print(f"{prod_token}")

