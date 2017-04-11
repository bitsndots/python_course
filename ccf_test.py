#!/usr/bin/python
import sys
from ciscoconfparse import CiscoConfParse as ccf

cisco_conf = ccf("/home/eriha/pynet/pyth_ans_ecourse/class1/cisco_ipsec.txt")

for object in cisco_conf.find_objects_w_child(parentspec=r"crypto map CRYPTO",childspec=r"pfs group2"):
    print "Object:", object
    print "Config text:", object.text

    for child in object:
        print child.text

quit()
