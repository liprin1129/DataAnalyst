import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict
from tqdm import tqdm

#osm_file = "data/sample.osm"
osm_file = "data/ex_VUBsnvgfVzCHpyoxLhnTYrc64M3F8.osm"

def count_tags(file_name):
    node_types = defaultdict(int)
    
    for event, elem in tqdm(ET.iterparse(file_name)):
        node_types[elem.tag] += 1

    #print(dict(node_types))

    return node_types

tags_dict = count_tags(osm_file)

print(tags_dict)
'''
import xml.etree.cElementTree as ET

def perf_func(elem, func, level=0):
    func(elem,level)
    for child in elem.getchildren():
        perf_func(child, func, level+1)

def print_level(elem,level):
    print '-'*level+elem.tag

root = ET.parse(osm_file)
perf_func(root.getroot(), print_level)
'''
