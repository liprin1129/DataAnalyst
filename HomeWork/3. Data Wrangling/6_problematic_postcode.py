# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:06:23 2017

@author: 170
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
from tqdm import tqdm
import re

#OSM_FILE = "data/Sheffield/3000_sample.osm"
#OSM_FILE = "data/Sheffield/ex_S1C26jUbkHMaYxNLf4RAcdFsdc4vy.osm"
#OSM_FILE = 'data/Sheffield/'+sys.argv[1]
OSM_FILE = "sample.osm"

postcode_re1 = re.compile(r'^\w\d\s\d\w{2}$', re.IGNORECASE)
postcode_re2 = re.compile(r'^\w\d\d+\s\d\w{2}$', re.IGNORECASE)
postcode_re3 = re.compile(r'^\w\d\s\d\d\w{2}$', re.IGNORECASE)
postcode_re4 = re.compile(r'^\w\d\d\s\d\d\w{2}$', re.IGNORECASE)

wrong_postcode = {}

def is_postcode(elem):
    return (elem.attrib['k'] == "addr:postcode")

def audit_wrong_postcode(postcode_dict, changeset, postcode):
    m1 = postcode_re1.search(postcode)
    m2 = postcode_re2.search(postcode)
    m3 = postcode_re3.search(postcode)
    m4 = postcode_re4.search(postcode)
    try:
        m1.group()
        m2.group()
        m3.group()
        m4.group()
    except:
        print postcode
        #postcode_dict[changeset].add(postcode)

def audit_postcode(file_in):
    street_types = defaultdict(set)
    
    with open(file_in, "r") as osm_file:        
        for event, elem in tqdm(ET.iterparse(osm_file, events=("start",))):

            if elem.tag == 'node' or elem.tag == "way":                                
                for tag in elem.iter("tag"):
                    if is_postcode(tag):
                        audit_wrong_postcode(wrong_postcode, elem.attrib['changeset'], tag.attrib["v"])

    return street_types

problematic_postcode = audit_postcode(OSM_FILE)
for key, street_name in problematic_postcode.iteritems():
    print key, street_name
