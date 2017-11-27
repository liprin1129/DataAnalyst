import xml.etree.cElementTree as ET
from collections import defaultdict
from tqdm import tqdm
import re


street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Crescent"]

additional = ['Hill', 'Way', 'Gate', 'Commons', 'East', 'Bank', 'Rise', 'Green', 'North', 'Gardens', 'South', 
              'View', 'walk', 'Walk', 'Close', 'Row']
              
unique_name = ['Smithfield', 'Crookes', 'The Dale', 'Dovecott Lea', 'Silver Street Head', 'Moor Valley', 
               'Rutland Park', 'Commonside', 'Wicker', 'Berkeley Precinct', 'Haymarket', 'Backfields',
               'Shalesmoor', 'Birkendale', 'The Crofts', 'Moorfields']

delete_name = ["Edmund Road Business Centre", "Riverside Park Industrial Estate", 
          "Sheaf Gardens Industrial Estate", "Waterthorpe Greenway", 
          "Sheaf Gardens Industrial Estate", "Sheffield Digital Campus"]
# UPDATE THIS VARIABLE
mapping = { "St.": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
            "rd" : "Road",
            "Utah Terrace": "Utah Road",
            "Westgate": "West Street",
            "462": "462 London road",
            "Upperthorpe": "Upperthorpe road",
            "Mount Pleasant Park": "Mount Pleasant Road",
            "Archer Road Retail Park": "Archer Road",
            "Victoria Villas": "Victoria Road"
            }

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
        
        remove_flag = False # check whether a element need to be deleted
        wrong_name_flag = False # 
        
        if street_name in delete_name:
            remove_flag = True
            
        elif ((street_type not in expected ) and 
            (street_type not in additional) and
            (street_type not in unique_name)):
            #if street_type not in additional:
            #    if street_type not in unique_name:
            #print(street_type, len(street_type))
            #street_types[street_type].add(street_name)
            # print(street_name)
            wrong_name_flag = True
            
        else:
            street_types[street_type].add(street_name)
            
        return remove_flag, wrong_name_flag
                
def audit_street_name(file_in):
    street_types = defaultdict(set)
    
    with open(file_in, "r") as osm_file:
        context = ET.iterparse(osm_file, events=("start", "end"))
        eventt, root = context.next()
        
        for event, elem in tqdm(context):
            if (elem.tag == 'node' or elem.tag == "way") and event == 'end':
                for tag in elem.iter("tag"):
                    if is_street_name(tag):
                        remove_flag, wrong_flag = audit_street_type(street_types, 
                                                        tag.attrib["v"])
                        
                        ## delete element if street is not in Sheffield
                        if remove_flag == True:
                            elem.clear()
                            
                        elif wrong_flag == True:
                            tag.attrib["v"] = update_name(tag.attrib["v"], mapping)
    
    return street_types

def update_name(name, mapping):
    #pprint.pprint(name)
    
    street_type_compiler = re.compile(r'\w+\S*$', re.IGNORECASE)
    
    wrong_name_obj = street_type_compiler.search(name)
    wrong_name_str = wrong_name_obj.group()
    
    #pprint.pprint(street_type_compiler.sub('Avenue', name)) # example
    #pprint.pprint(street_type_compiler.sub(mapping[wrong_name_str], name))
    
    name = street_type_compiler.sub(mapping[wrong_name_str], name)
    return name
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
    #OSM_FILE = 'data/Sheffield/Sheffield_data.osm'
    OSM_FILE = "data/Sheffield/sample.osm"
    
    problematic_street_name = audit_street_name(OSM_FILE)
    for key, street_name in problematic_street_name.iteritems():
        print key, street_name
