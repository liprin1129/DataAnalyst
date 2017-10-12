import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict
from tqdm import tqdm
from datetime import datetime
from dateutil.parser import parse

OSM_FILE = "data/Sheffield/3000_sample.osm"
ATTRIB_KEY = ['changeset', 'uid', 'timestamp', 'lon', 'versioin', 'user', 'lat', 'id']

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        pass
    
    try:
        import unicodedata
        unicodedata.numeric(string)
        return True
    except (TypeError, ValueError):
        pass
    
    return False

def is_date(string):
    try: 
        parse(string)
        return True
    except ValueError:
        return False

def type_check(key, value, return_dict):
    # Check if number
    if is_number(value):# and attr in ATTRIB_KEY:
        if value.isdigit(gg):
            return_dict[key].add(type(int()))
            #print('{0:5} -- int: {1}'.format('', fieldtypes[field]))
        else:
            return_dict[key].add(type(float()))
            #print('{0:5} -- float: {1}'.format('', fieldtypes[field]))                        
            # Check if date timestamp
    elif is_date(value):
        return_dict[key].add(type(datetime.now()))
        
        # Check if empty
    elif key == 'NULL' or key == '':
        return_dict[key].add(type(None))
        
        # Check if array
    elif value.startswith('{') or value.startswith('(') or value.startswith('['):
        return_dict[key].add(type(list()))
        
        # Otherwise string
    else:
        return_dict[key].add(type(str()))
    
def audit_attrib_type(file_in):
    node_attribs = defaultdict(set)
    nd_attribs = defaultdict(set)
    member_attribs = defaultdict(set)
    tag_attribs = defaultdict(set)
    relation_attribs = defaultdict(set)
    way_attribs = defaultdict(set)
    
    for event, elem in tqdm(ET.iterparse(file_in)):
        if elem.tag == 'node':
            #print '\n'
            
            for attr in elem.attrib:
                type_check(attr, elem.attrib[attr], node_attribs)
                #print attr, elem.attrib[attr]
                '''
                # Check if number
                if is_number(elem.attrib[attr]):# and attr in ATTRIB_KEY:
                    if attr.isdigit():
                        attrib_types[attr].add(type(int()))
                        #print('{0:5} -- int: {1}'.format('', fieldtypes[field]))
                    else:
                        attrib_types[attr].add(type(float()))
                        #print('{0:5} -- float: {1}'.format('', fieldtypes[field]))                        
                # Check if date timestamp
                elif is_date(elem.attrib[attr]):
                    attrib_types[attr].add(type(datetime.now()))

                # Check if empty
                elif elem.attrib[attr] == 'NULL' or elem.attrib[attr] == '':
                    attrib_types[attr].add(type(None))

                # Check if array
                elif elem.attrib[attr].startswith('{') or elem.attrib[attr].startswith('(') or elem.attrib[attr].startswith('['):
                    attrib_types[attr].add(type(list()))

                # Otherwise string
                else:
                    attrib_types[attr].add(type(str()))
                '''

        if elem.tag == 'nd':
            for attr in elem.attrib:                
                type_check(attr, elem.attrib[attr], nd_attribs)

        if elem.tag == 'member':
            for attr in elem.attrib:                
                type_check(attr, elem.attrib[attr], member_attribs)
                
        if elem.tag == 'tag':
            for attr in elem.attrib:                
                type_check(attr, elem.attrib[attr], tag_attribs)

        if elem.tag == 'relation':
            for attr in elem.attrib:                
                type_check(attr, elem.attrib[attr], relation_attribs)

        if elem.tag == 'way':
            for attr in elem.attrib:                
                type_check(attr, elem.attrib[attr], way_attribs)

    print '< node >'
    for key, value in node_attribs.iteritems():
        print key, ':', value

    print '\n', '< nd >'
    for key, value in nd_attribs.iteritems():
        print key, ':', value

    print '\n', '< member >'
    for key, value in member_attribs.iteritems():
        print key, ':', value

    print '\n', '< tag >'
    for key, value in tag_attribs.iteritems():
        print key, ':', value

    print '\n', '< relation >'
    for key, value in relation_attribs.iteritems():
        print key, ':', value

    print '\n', '< way >'
    for key, value in way_attribs.iteritems():
        print key, ':', value        

if __name__ == '__main__':
    audit_attrib_type(OSM_FILE)
