#!/usr/bin/python

import yaml
import sys

my_list = ["pizza","pasta","fish","antipasti"]
my_list.append({})

my_list[-1]['vegetables'] = 'zucchini'
my_list[-1]['meat'] = 'chicken'
my_list.append(range(10))

with open("output.yml","w") as of:
    of.write(yaml.dump(my_list,default_flow_style=False))

sys.exit(0)
