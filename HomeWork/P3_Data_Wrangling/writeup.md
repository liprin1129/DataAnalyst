# OpenStreetMap Data Case Study

I investigated Sheffield in the UK where I am familiar with, and do some basic data wrangling tasks according to the steps below,

1. query database
2. audit the data
3. 

This map is of my hometown, so I’m more interested to see what database querying reveals, and I’d like an opportunity to contribute to its improvement on OpenStreetMap.org.

## 1. Data Audit

#### 1.1. Unique tags
For the first data audit task, '1\_unique\_tags.py' counts the number of unique tags.

Name | Count
------------ | -------------
node         | 1082390
nd           | 1395801
bounds       | 1
member       | 23781
tag          | 431569
relation     | 2196
way          | 174004
osm          | 1

**node**, **nd**, **member**, **tag**, **relation**, and **way** seem having resoanable number of counts. 

#### 1.2. Attributes types

So I checked the type of attribtues of those elements for consistency of the data. 

```Python
< node >
	changeset : set([<type 'int'>])
	uid : set([<type 'int'>])
	timestamp : set([<type 'datetime.datetime'>])
	lon : set([<type 'float'>])
	version : set([<type 'int'>])
	user : set([<type 'str'>])
	lat : set([<type 'float'>])
	id : set([<type 'int'>])
	
< nd >
	ref : set([<type 'int'>])
	
< member >
	ref : set([<type 'int'>])
	role : set([<type 'str'>])
	type : set([<type 'str'>])
	
< tag >
	k : set([<type 'str'>])
	v : set([<type 'int'>, <type 'str'>])
	
< relation >
	changeset : set([<type 'int'>])
	uid : set([<type 'int'>])
	timestamp : set([<type 'datetime.datetime'>])
	version : set([<type 'int'>])
	user : set([<type 'str'>])
	id : set([<type 'int'>])
	
< way >
	changeset : set([<type 'int'>])
	uid : set([<type 'int'>])
	timestamp : set([<type 'datetime.datetime'>])
	version : set([<type 'int'>])
	user : set([<type 'str'>])
	id : set([<type 'int'>])
```

A type of major nodes seems not including critical problems. All nodes have unique attribute value. However, attribute **v** in **tag** element has multiple types, and it seems to be concidered inconsistent data. Although the multiple types in **v** element, it is not a problematic case, because **tag** elements hold various kind of values accordingly different keys. For example,

```XML
    <tag k="name" v="Raeburn Road/Morland Drive" />
    <tag k="source" v="naptan_import" />
    <tag k="highway" v="bus_stop" />
    <tag k="alt_name" v="Raeburn Road/Morland Drive" />
    <tag k="naptan:Street" v="Raeburn Road" />
    <tag k="naptan:Bearing" v="N" />
    <tag k="naptan:AtcoCode" v="370026690" />
    <tag k="naptan:Landmark" v="Bottom of Steps" />
```

Above code has 8 different keys for **k** of tag element's attribute; **name, source, highway, alt_name, naptan:Street, naptan:Bearing, naptan:AtcoCode, naptan:Landmark**, and types of those values are either strings or numbers. 

#### 1.3. Key and value of tag attributes

To know whether the elements are meaningfule, in other words what kind of information in elements is the most dominant, I counted the number of their children in accordance with tag names.

node                        | relation                  | way
--------------------------- | ------------------------- | ----------------------
highway: 7767               | type: 2111                | 	building: 112076
name: 6184                  | name: 1661                | source: 92744
source: 5742                | source: 1514              | highway: 38054
naptan:Street: 3800         | site: 1460                | name: 20406
naptan:AtcoCode: 3793       | naptan:verified: 1448     | landuse: 8769
naptan:Landmark: 3771       | naptan:StopAreaCode: 1445 | addr:housenumber: 4076
naptan:verified: 3760       | naptan:StopAreaType: 1443 | barrier: 3709
naptan:Indicator: 3749      | restriction: 206          | surface: 3569
naptan:CommonName: 3742     | route: 169                | addr:street: 3099
naptan:Bearing: 3729        | operator: 144             | oneway: 2958
naptan:PlusbusZoneRef: 3660 | ref: 141                  | natural: 2794
created_by: 2983            | building: 80              | maxspeed: 2784
...                         | ...                       | ...

Interestingly, there were no additional children tag in **member** and **nd** elements, while **node**, **tag**, and **relation** have many additional information.

**node**, **relation**, and **way** elements contain children nodes called tag, but they are not included in **member** and **nd** elements. In other words, there are no additional information in **member** and **nd** elements, while **node**, **tag**, and **relation** have many additional information conceived in sub-nodes, tag. Thus, I only focus the further audit tasks on those three elements.

## 2. Problems Encountered in the Map Dataset

#### 2.1. Problems in street name
In Sheffield, there are many unique road types which go beyond the given basic types; *Street, Avenue, Boulevard, Drive, Court, Place, Square, Lane*, and *Road*, for example *Upperthorpe Glen*, and *Fargate*. So after I implemented a code (problematic\_street\_name.py) which tells about unique street names, in other world not be included in the given basic road type list, I searched the unique street names on Google map, and checked if they are really unique name or mistyped name.

- Building name: 
	- Edmund Road Business Centre
	- Fargate

- Not in Sheffield:
	- Riverside Park Industrial Estate
	- Sheaf Gardens Industrial Estate

- Abbrebiation: 
	- rd -> Road

- Not in Sheffield: 
	- Waterthorpe Greenway is in Westfield
	- Sheaf Gardens Industrial Estate in Middlesbrough
	- Sheffield Digital Campus (no where)

- duplicated:
	- Barker's Pool and Barkers Pool
	- Utah Terrace and Utah terrace

- Wrong name: 
	- Utah Terrace -> Utah Road
	- Westgate -> West Street
	- 462 -> 462 London road (not sure)
	- Upperthorpe -> Upperthorpe road
	- Mount Pleasant Park -> Mount Pleasant Road
	- Archer Road Retail Park -> Archer Road
	- Victoria Villas -> Victoria Road or Victoria Street

- Additional Road Type:
	- Green
	- East 
	- North
	- Green
	- East
	- North
	- Gardens
	- South
	- West
	- View
	- Walk
	- Row
	- Close
	- Common
	- Gate
	- Grove
	- Head
	- Hill
	- Mount
	- Parade
	- Pool
	- Rise
	- Row
	- View
	- Crooks
	- Park
	- Bank
	- Lea

- Unique Road Name:
	- Crookes
	- Backfields
	- Shalesmoor
	- Birkendale
	- The Crofts
	- Moorfields
	- Rutland Park
	- West Bar
	- Commonside
	- Crescent
	- The Dale
	- Upperthorpe Glen
	- Waterthorpe Greenway
	- Hartshead
	- Haymarket
	- Busk Knoll
	- Meadowhead
	- The Moor
	- Moorfields
	- Berkeley Precinct
	- Upperthorpe
	- Moor Valley
	- Wicker
	- Rutland Park
	- Smithfield


In problematic\_street\_name.py, I added the two lists (**unique** and **additional**) which refer unique road names and additional road types respectively, along side with the given expected road name list. I also made a list of names (removed) which are not in Sheffield or building names. Finally, I filled the **mapping** list to convert wrong street types and names to correct ones.

#### 2.2. Problems in postal code

All buildings sould have specific postal code. Each group has alphabet and numbers. The UK postal code are consisted of two groups. The first group starts with an alphabet followed by number or numbers. The second one has a reversed order. So, postal codes should have a form like S10 1FG.

In *6\_problematic\_postcode.py*, I auditted **addr:postcode** in sub-nodes named tag, and found 43 postal codes that there are building but do not conform the rule. 

 postal code| id
----------- | ------------ 
S12 | 105817698, 105817704, 105817710, 112003218
S10 | 229282360
S17 | 102871594
S12 2 | 101781200, 101783948, 101783949, 103789013, 101783953, 
S12 2 | 101783958, 101781191, 101781193, 101781178, 103788969, 
S12 2| 103788976, 103788981, 101781174, 101781154, 101783954, 
S12 2 | 101781151, 100153189, 100153186, 100153187, 100153184, 
S12 2 | 100153185, 101781159, 100153183, 101783951, 101783950, 
S12 2 | 103789002, 103789006, 101781182, 105190682, 101781186, 
S12 2 | 103788994, 101781166, 101781189, 101781161])
S6 | 107368123, 107368125
S9 5 | 106300879

There is no way to correct those postal codes, unless I visit there and identify whether the postal codes are correct or not personally. Therefore, I removed the ids above containing wrong postal codes just for data's completeness.

#### 2.3. Data cleaning

Based on the problems audited above, I cleaned and corrected the dataset. For problamatic street name, I removed the street names which are not in Sheffield, so they have **None** value in their nodes. Then I modified wrong street name and street type. Finally, duplicated street type is also deleted. Below is the snip code for street name cleaning process.

```Python
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
```
Next, posecodes were just removed if they are incorrect, because correcting those postcodes would take many efforts. Thus, for this project, it's better to just discard.

```Python
def update_wrong_postcode(postcode):
    postcode_re1 = re.compile(r'^\w\d\s\d\w{2}$', re.IGNORECASE)
    postcode_re2 = re.compile(r'^\w\d\d+\s\d\w{2}$', re.IGNORECASE)
    postcode_re3 = re.compile(r'^\w\d\s\d\d\w{2}$', re.IGNORECASE)
    postcode_re4 = re.compile(r'^\w\d\d\s\d\d\w{2}$', re.IGNORECASE)
    
    m1 = postcode_re1.search(postcode)
    m2 = postcode_re2.search(postcode)
    m3 = postcode_re3.search(postcode)
    m4 = postcode_re4.search(postcode)

    if m1:
        return postcode
    elif m2:
        return postcode
    elif m3:
        return postcode
    elif m4:
        return postcode
    else:
        return
```

The snip codes are in '5\_problematic\_street\_name.py' and '6\_problematic\_postcode.py' respectively. I said 'remove' and 'delete' data, but it actually doesn't mean 'remove child nodes'. I will explain it in detail in the next section.

## 3. Save Dataset to SQL Database

#### Snip code explanation
This is the task that I spent much time than other tasks. With the cleaning schemes above, I investigated each row which is given by *iterparse* function of *ElementTree* whether which is the problematic one. By iterating the whole dataset row by row, I could evade memory consumption issue compared to when I loaded whole dataset using *parse* function. 

If a row is about street name or postcode, I checked and modified problematic ones if they are not those which have to be removed. Just not including them to tags dictionary which are to be converted to SQL database, I could actually discard (or neglect) them. 

```Python
if is_street_name(tag_node):
	street_name = audit_street_type_for_data_py(tag_node.attrib['v'])
	if street_name:
		tag['id'] = element.attrib['id']
		tag['value'] = street_name

		try:
			key_value = re.findall(r'([a-z]+):(.+$)', tag_k)
			tag['key'] = key_value[0][1]
			tag['type'] = key_value[0][0]
		except:
			tag['key'] = tag_node.attrib['k']
			tag['type'] = 'regular'
		tags.append(tag)

elif is_postcode(tag_node):
	postcode = update_wrong_postcode(tag_node.attrib['v'])
	if postcode:
		tag['id'] = element.attrib['id']
		tag['value'] = postcode 
	
		try:
			key_value = re.findall(r'([a-z]+):(.+$)', tag_k)
			tag['key'] = key_value[0][1]
			tag['type'] = key_value[0][0]
		except:
			tag['key'] = tag_node.attrib['k']
			tag['type'] = 'regular'
		tags.append(tag)
```

With the pure dataset, I firstly converted it into csv format and then finally to SQL database. It is in '7\_xml\_to\_csv.py', and '8\_csv2sql\_db.py', respectively.

#### Data size
This is an outline of file size though data wrangling and converting tasks.

```
Sheffield_data.osm .......... 240.5 MB
                ⬇
nodes_tags.csv .............. 3 MB
nodes.csv ................... 89.7 MB
ways_nodes.csv .............. 33.4 MB
ways_tags.csv ............... 11.4 MB
ways.csv .................... 10.5 MB
                ⬇
street_data.db .............. 134.8 MB
```

## 4. Explore Database

#### Tables in database

```sql
sqlite> .tables
node	node_tags	way	way_nodes	way_tags 
```

#### Total number of nodes
```sql
sqlite> SELECT COUNT(*) FROM node;
1082172
```

#### Total number of ways
```
sqlite> SELECT COUNT(*) FROM way;
173982
```

<!-------------->
<!-- Template -->
<!-------------->

### Postal Codes
Postal code strings posed a different sort of problem, forcing a decision to strip all leading and trailing characters before and after the main 5­digit zip code. This effectively dropped all leading state characters (as in “NC28226”) and 4­digit zip code extensions following a hyphen (“28226­0783”). This 5­digit restriction allows for more consistent queries.


Regardless, after standardizing inconsistent postal codes, some altogether “incorrect” (or perhaps misplaced?) postal codes surfaced when grouped together with this aggregator:

```sql
SELECT tags.value, COUNT(*) as count 
FROM (SELECT * FROM nodes_tags 
	  UNION ALL 
      SELECT * FROM ways_tags) tags
WHERE tags.key='postcode'
GROUP BY tags.value
ORDER BY count DESC;
```

Here are the top ten results, beginning with the highest count:

```sql
value|count
28205|900
28208|388
28206|268
28202|204
28204|196
28216|174
28211|148
28203|120
28209|104
28207|86
```

 These results were taken before accounting for Tiger GPS zip codes residing in second­ level “k” tags. Considering the relatively few documents that included postal codes, of those, it appears that out of the top ten, seven aren’t even in Charlotte, as marked by a “#”. That struck me as surprisingly high to be a blatant error, and found that the number one postal code and all others starting with“297”lie in Rock Hill, SC. So, I performed another aggregation to verify a certain suspicion...
# Sort cities by count, descending

```sql
sqlite> SELECT tags.value, COUNT(*) as count 
FROM (SELECT * FROM nodes_tags UNION ALL 
      SELECT * FROM ways_tags) tags
WHERE tags.key LIKE '%city'
GROUP BY tags.value
ORDER BY count DESC;
```

And, the results, edited for readability:

```sql
Rock Hill   111       
Pineville   27        
Charlotte   26        
York        24        
Matthews    10        
Concord     4         
3000        3         
10          2         
Lake Wylie  2         
1           1         
3           1         
43          1         
61          1         
Belmont, N  1         
Fort Mill,  1         
```

These results confirmed my suspicion that this metro extract would perhaps be more aptly named “Metrolina” or the “Charlotte Metropolitan Area” for its inclusion of surrounding cities in the sprawl. More importantly, three documents need to have their trailing state abbreviations stripped. So, these postal codes aren’t “incorrect,” but simply unexpected. However, one final case proved otherwise.
A single zip code stood out as clearly erroneous. Somehow, a “48009” got into the dataset. Let’s display part of its document for closer inspection (for our purposes, only the “address” and “pos” fields are relevant):

```sql
sqlite> SELECT *
FROM nodes 
WHERE id IN (SELECT DISTINCT(id) FROM nodes_tags WHERE key='postcode' AND value='48009')
```
`1234706337|35.2134608|-80.8270161|movercash|433196|1|7784874|2011-04-06T13:16:06Z`

`sqlite> SELECT * FROM nodes_tags WHERE id=1234706337 and type='addr';`

```sql
1234706337|housenumber|280|addr
1234706337|postcode|48009|addr
1234706337|street|North Old Woodward Avenue|addr
```

 It turns out, *“280 North Old Woodward Avenue, 48009”* is in Birmingham, Michigan. All data in this document, including those not shown here, are internally consistent and verifiable, except for the latitude and longitude. These coordinates are indeed in Charlotte, NC. I’m not sure about the source of the error, but we can guess it was most likely sitting in front of a computer before this data entered the map. The document can be removed from the database easily enough.

# Data Overview and Additional Ideas
This section contains basic statistics about the dataset, the MongoDB queries used to gather them, and some additional ideas about the data in context.

### File sizes
```
charlotte.osm ......... 294 MB
charlotte.db .......... 129 MB
nodes.csv ............. 144 MB
nodes_tags.csv ........ 0.64 MB
ways.csv .............. 4.7 MB
ways_tags.csv ......... 20 MB
ways_nodes.cv ......... 35 MB  
```  

### Number of nodes
```
sqlite> SELECT COUNT(*) FROM nodes;
```
1471350

### Number of ways
```
sqlite> SELECT COUNT(*) FROM ways;
```
84502

### Number of unique users
```sql
sqlite> SELECT COUNT(DISTINCT(e.uid))          
FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e;
```
337

### Top 10 contributing users
```sql
sqlite> SELECT e.user, COUNT(*) as num
FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e
GROUP BY e.user
ORDER BY num DESC
LIMIT 10;
```

```sql
jumbanho    823324    
woodpeck_f  481549    
TIGERcnl    44981     
bot-mode    32033     
rickmastfa  18875     
Lightning   16924     
grossing    15424     
gopanthers  14988     
KristenK    11023     
Lambertus   8066 
```
 
### Number of users appearing only once (having 1 post)
```sql
sqlite> SELECT COUNT(*) 
FROM
    (SELECT e.user, COUNT(*) as num
     FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e
     GROUP BY e.user
     HAVING num=1)  u;
```
56

# Additional Ideas

## Contributor statistics and gamification suggestion 
The contributions of users seems incredibly skewed, possibly due to automated versus manual map editing (the word “bot” appears in some usernames). Here are some user percentage statistics:

- Top user contribution percentage (“jumbanho”) 52.92%
- Combined top 2 users' contribution (“jumbanho” and “woodpeck_fixbot”) 83.87%
- Combined Top 10 users contribution
94.3%
- Combined number of users making up only 1% of posts 287 (about 85% of all users)

Thinking about these user percentages, I’m reminded of “gamification” as a motivating force for contribution. In the context of the OpenStreetMap, if user data were more prominently displayed, perhaps others would take an initiative in submitting more edits to the map. And, if everyone sees that only a handful of power users are creating more than 90% a of given map, that might spur the creation of more efficient bots, especially if certain gamification elements were present, such as rewards, badges, or a leaderboard. 

## Additional Data Exploration

### Top 10 appearing amenities

```sql
sqlite> SELECT value, COUNT(*) as num
FROM nodes_tags
WHERE key='amenity'
GROUP BY value
ORDER BY num DESC
LIMIT 10;
```

```sql
place_of_worship  580       
school            402       
restaurant        80        
grave_yard        75        
parking           63        
fast_food         51        
fire_station      48        
fuel              31        
bench             30        
library           28 
```

### Biggest religion (no surprise here)

```sql
sqlite> SELECT nodes_tags.value, COUNT(*) as num
FROM nodes_tags 
    JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='place_of_worship') i
    ON nodes_tags.id=i.id
WHERE nodes_tags.key='religion'
GROUP BY nodes_tags.value
ORDER BY num DESC
LIMIT 1;
```
`christian   571`

### Most popular cuisines

```sql
sqlite> SELECT nodes_tags.value, COUNT(*) as num
FROM nodes_tags 
    JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='restaurant') i
    ON nodes_tags.id=i.id
WHERE nodes_tags.key='cuisine'
GROUP BY nodes_tags.value
ORDER BY num DESC;
```

```sql
american    9         
pizza       5         
steak_hous  4         
chinese     3         
japanese    3         
mexican     3         
thai        3         
italian     2         
sandwich    2         
barbecue    1
```

# Conclusion
 After this review of the data it’s obvious that the Charlotte area is incomplete, though I believe it has been well cleaned for the purposes of this exercise. It interests me to notice a fair amount of GPS data makes it into OpenStreetMap.org on account of users’ efforts, whether by scripting a map editing bot or otherwise. With a rough GPS data processor in place and working together with a more robust data processor similar to data.pyI think it would be possible to input a great amount of cleaned data to OpenStreetMap.org.
