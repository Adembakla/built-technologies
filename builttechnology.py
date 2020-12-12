#!/usr/bin/env python
# coding: utf-8

# Problem:
# 1. Takes an IP address as a command line argument
# 2. Gets json data from the RIPE network coordination center link here
# 3. Use the ['data']['resources']['ipv4'] block in the json above to determine whether the IP provided on the CLI is in any of the CIDRs
# 4. Output a Pass/Fail result based on the presence of the IP address in the CIDR ranges

# How to run: 
# python check_ip_address.py '2.57.164.0/22' 

# output: Pass or Fail depends on the ip address whether in data.json or not

import sys
import json

# parse ip address from args
ip_address = sys.argv[1]

# Opening JSON file 
f = open('data.json',) 
  
# returns JSON object as a dictionary 
data = json.load(f) 

# Output
if ip_address in data['data']['resources']['ipv4']:
    print('Pass')
else:
    print('Fail')
