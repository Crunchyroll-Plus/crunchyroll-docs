#!/usr/bin/python
from dump_basic import prod, get_b64
from os import path, listdir

import re

project_directory = path.dirname(path.dirname(__file__)) 
auth_directory = path.join(project_directory, "Services/EtpAccountAuth/POST")

for file in listdir(auth_directory):
    fp = path.join(auth_directory, file)
    text = ""
    with open(fp, "r") as fr:
        text = re.sub(r': Basic [\w=-]+', f": Basic {get_b64(prod)}", fr.read())
    
    if text == "":
        continue

    with open(fp, "w") as fw:
        fw.write(text)

    print(f"Updated {fp}") 
