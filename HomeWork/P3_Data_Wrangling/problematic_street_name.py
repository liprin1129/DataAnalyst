import xml.etree.cElementTree as ET
from collections import defaultdict
from tqdm import tqdm
import re
import pprint

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Way"]

additional = ["Green", "East", "North", "Gardens", "South", "View", "Walk", 
              "Row", "Close", "Common", "Gate", "Grove", "Head", "Hill", 
              "Mount", "Parade", "Pool", "Rise", "Row", "View", "Bank", "Crescent", "Lea", "West", "Terrace"]

unique = ["Crookes", "Backfields", "Shalesmoor", "Birkendale", "The Crofts", 
          "Moorfields", "Rutland Park", "West Bar", "Commonside", "Crescent", 
          "The Dale", "Upperthorpe Glen", "Waterthorpe Greenway", "Hartshead", 
          "Haymarket", "Busk Knoll", "Meadowhead", "The Moor", "Moorfields", 
          "Berkeley Precinct", "Upperthorpe", "Moor Valley", "Wicker", "Rutland Park", "Smithfield"]

removed = ["Sheffield Digital Campus", "Edmund Road Business Centre", 
           "Riverside Park Industrial Estate", "Sheaf Gardens Industrial Estate",
           "Utah terrace", "Fargate"]

mapping_type = { "St.": "Street",
                "Ave": "Avenue",
                "Rd.": "Road",
                "rd": "Road"}

mapping_name = {"Archer Road Retail Park": "Archer Road",
                "Mount Pleasant Park": "Mount Pleasant Road",
                "Victoria Villas": "Victoria Road or Victoria Street",
                "Westgate": "West Street",
                "462": "462 London road"}

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_name in unique:
            return False
        
        elif (street_name in removed):
            #print(True, street_type,":", street_name)
            return True
        
        elif street_name in mapping_name.keys():
            return update_name(street_name, mapping_name)
        
        elif street_type in mapping_type.keys():
            return update_type(street_name, mapping_type)
        
        elif ((street_type not in expected ) and 
             (street_type not in additional)):
             street_types[street_type].add(street_name)
             return False
    #pprint.pprint(street_types)

def audit_street_type_for_data_py(street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_name in unique:
            return street_name
        
        elif (street_name in removed):
            #print(True, street_type,":", street_name)
            return
        
        elif street_name in mapping_name.keys():
            return update_name(street_name, mapping_name)
        
        elif street_type in mapping_type.keys():
            return update_type(street_name, mapping_type)
        
        else:
            return street_name

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit_type(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in tqdm(ET.iterparse(osm_file, events=("start",))):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    street = tag.attrib['v'] # name of street
                    
                    '''
                    if street in mapping.keys():
                        street = update_name(street, mapping)
                    '''
                    
                    returned_value = audit_street_type(street_types, street)

                    if returned_value == True:
                        elem.clear()
                        
                    elif type(returned_value) == str:
                        street = returned_value
                        
    osm_file.close()
    return street_types


def update_name(name, mapping):
    #pprint.pprint(name)
    
    #street_type_compiler = re.compile(r'\w+\S*$', re.IGNORECASE)
    
    #wrong_name_obj = street_type_compiler.search(name)
    #wrong_name_str = wrong_name_obj.group()
    
    #pprint.pprint(street_type_compiler.sub('Avenue', name)) # example
    #pprint.pprint(street_type_compiler.sub(mapping[wrong_name_str], name))
    
    name = mapping[name]
    return name

def update_type(name, mapping):
    #pprint.pprint(name)
    
    street_type_compiler = re.compile(r'\w+\S*$', re.IGNORECASE)
    
    wrong_name_obj = street_type_compiler.search(name)
    wrong_name_str = wrong_name_obj.group()
    #pprint.pprint(wrong_name_str)
    
    #pprint.pprint(street_type_compiler.sub('Avenue', name)) # example
    #pprint.pprint(street_type_compiler.sub(mapping[wrong_name_str], name))
    
    name = street_type_compiler.sub(mapping[wrong_name_str], name)
    return name


def test():
    st_types = audit_type(OSMFILE)
    #assert len(st_types) == 3
    pprint.pprint(dict(st_types))
    
    '''
    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name
            if name == "West Lexington St.":
                assert better_name == "West Lexington Street"
            if name == "Baldwin Rd.":
                assert better_name == "Baldwin Road"
    '''
    
if __name__ == '__main__':
    OSMFILE = "data/Sheffield/sample.osm"
    #OSMFILE = 'data/Sheffield/Sheffield_data.osm'
    test()
