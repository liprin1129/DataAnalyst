import xml.etree.cElementTree as ET
from collections import defaultdict
from tqdm import tqdm
import re


street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Crescent"]

additional = ['Hill', 'Way', 'Gate', 'Commons', 'East', 'Bank', 'Rise', 'Green', 'North', 'Gardens', 'South', 
              'View', 'walk', 'Close', 'Row']
              
unique_name = ['Smithfield', 'Crookes', 'The Dale', 'Dovecott Lea', 'Silver Street Head', 'Moor Valley', 
               'Rutland Park', 'Commonside', 'Wicker', 'Berkeley Precinct', 'Haymarket', 'Backfields',
               'Shalesmoor', 'Birkendale', 'The Crofts', 'Moorfields']

'''
def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types
'''

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
          
def audit_street_name(file_in):
    street_types = defaultdict(set)
    
    with open(file_in, "r") as osm_file:        
        for event, elem in tqdm(ET.iterparse(osm_file, events=("start",))):

            if elem.tag == 'node' or elem.tag == "way":                                
                for tag in elem.iter("tag"):
                    if is_street_name(tag):
                        audit_street_type(street_types, tag.attrib["v"])

    return street_types
'''
def print_street_name(file_in):
    with open(file_in, 'r') as osm_file:
        for event, elem in tqdm(ET.iterparse(osm_file, events=("start",))):
            if elem.tag == 'node' or elem.tag == "way":                                
                for tag in elem.iter("tag"):
                    if is_street_name(tag):
                        #audit_street_type(street_types, tag.attrib["v"])
                        print tag.attrib['v']

def audit_key_name(file_in):
    node_dict = defaultdict(int)
    nd_dict = defaultdict(int)
    member_dict = defaultdict(int)
    relation_dict = defaultdict(int)
    way_dict = defaultdict(int)
    
    with open(file_in, 'r') as osm_file:
        for event, elem in tqdm(ET.iterparse(osm_file, events=("start",))):

            if (elem.tag == 'node' or 'nd' or 'member' or 'relation' or 'way'):
                for tag_in in elem:
                    if tag_in.tag == 'tag':
                        #print elem.tag, ':', tag_in.attrib
                        eval('{0}_dict'.format(elem.tag))[tag_in.attrib['k']] += 1

    #return key_names
    return node_dict, nd_dict, member_dict, relation_dict, way_dict
'''

if __name__ == "__main__":
    #OSM_FILE = "data/Sheffield/3000_sample.osm"
    #OSM_FILE = "data/Sheffield/ex_S1C26jUbkHMaYxNLf4RAcdFsdc4vy.osm"
    OSM_FILE = 'data/Sheffield/Sheffield_data.osm'
    #OSM_FILE = "sample.osm"
    #OSM_FILE  = 'Sheffield_data.osm'
    
    problematic_street_name = audit_street_name(OSM_FILE)
    for key, street_name in problematic_street_name.iteritems():
        print key, street_name
