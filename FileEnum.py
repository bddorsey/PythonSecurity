#!/usr/bin/env python3

import requests
import sys

####Script for File enumeration####
# author: Brian Dorsey            #
# date: 1/7/22                    #
###################################



dir_list = open("files.txt").read()
directories = dir_list.splitlines()
counter = 0

for dir in directories:
    counter += 1
    dir_enum = f"http://{sys.argv[1]}/{dir}.html"
    r = requests.get(dir_enum)
    if r.status_code == 404:
        print(f"{counter}: {dir}: failed")

    else:
        print(f"Valid directory:{dir_enum}")