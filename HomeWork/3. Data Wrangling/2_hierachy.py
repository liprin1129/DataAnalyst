import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict
from tqdm import tqdm

#osm_file = "data/5000_sample.osm"
osm_file = "sample.osm"

def node_element(file_name):
    for event, elem in tqdm(ET.iterparse(file_name)):
        if elem.tag == "node":
            #for attr, value in event[2].items():
            #    print attr, value
            #print elem.attrib

            #print [x for x in elem if not x == None]
            child_node = [x for x in elem]
            if child_node:
                for tag in child_node:
                    print tag.attrib
                print 

node_element(osm_file)
