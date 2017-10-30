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
#OSM_FILE = "sample.osm"
OSM_FILE  = 'Sheffield_data.osm'

postcode_re1 = re.compile(r'^\w\d\s\d\w{2}$', re.IGNORECASE)
postcode_re2 = re.compile(r'^\w\d\d+\s\d\w{2}$', re.IGNORECASE)
postcode_re3 = re.compile(r'^\w\d\s\d\d\w{2}$', re.IGNORECASE)
postcode_re4 = re.compile(r'^\w\d\d\s\d\d\w{2}$', re.IGNORECASE)

wrong_postcode = {}

def is_postcode(elem):
    return (elem.attrib['k'] == "addr:postcode")

def audit_wrong_postcode(postcode_list, changeset_id, postcode, building):
    m1 = postcode_re1.search(postcode)
    m2 = postcode_re2.search(postcode)
    m3 = postcode_re3.search(postcode)
    m4 = postcode_re4.search(postcode)

    if not (m1 or m2 or m3 or m4) and building:
        #print postcode
        postcode_list[postcode].add(changeset_id)
    
def audit_postcode(file_in):
    postcode_name = defaultdict(set)
    
    with open(file_in, "r") as osm_file:        
        for event, elem in tqdm(ET.iterparse(osm_file, events=("start",))):

            if elem.tag == 'node' or elem.tag == "way":
                building = None
                for tag in elem.iter("tag"):
                    if tag.attrib['k'] == 'building':
                        building = tag.attrib['v']
                
                for tag in elem.iter("tag"): 
                    if is_postcode(tag):
                        audit_wrong_postcode(postcode_name, elem.attrib['id'], tag.attrib["v"], building)

    return postcode_name

problematic_postcode = audit_postcode(OSM_FILE)
for postcode, house_name in problematic_postcode.iteritems():
    print postcode, house_name #house_name