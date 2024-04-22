#!/usr/bin/env python3


####Script for sub-domain enumeration####
# author: Brian Dorsey                  #
# date: 1/4/22                          #
#########################################


import requests
import sys




sub_list = open("domains.txt").read()
subdoms = sub_list.splitlines()
counter = 0  #count the number of sub-domains attempts that failed

for sub in subdoms:
    counter += 1
    sub_domains = f"http://{sub}.{sys.argv[1]}"
    try:
        requests.get(sub_domains)

    except requests.ConnectionError:
        print(f"{counter}: {sub}: failed")

    else:
        print(f"Valid domain:{sub_domains}")#!/usr/bin/env python3

import requests
import sys

""" Script for sub-domain enumeration"""
#author: Brian Dorsey
#date: 1/4/22


sub_list = open("domains.txt").read()
subdoms = sub_list.splitlines()
counter = 0  #count the number of sub-domains attempts that failed

for sub in subdoms:
    counter += 1
    sub_domains = f"http://{sub}.{sys.argv[1]}"
    try:
        requests.get(sub_domains)

    except requests.ConnectionError:
        print(f"{counter}: {sub}: failed")

    else:
        print(f"Valid domain:{sub_domains}")