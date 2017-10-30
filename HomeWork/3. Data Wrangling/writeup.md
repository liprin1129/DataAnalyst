# OpenStreetMap Data Case Study

### Map Area
Izumo, Shimane, Japan
- [https://www.openstreetmap.org/relation/4088005#map=10/35.5216/132.7849](https://www.openstreetmap.org/relation/4088005#map=10/35.5216/132.7849)

I investigated an area where I am living in, and do some basic data wrangling tasks according to the steps below,

1. query database
2. audit the data
3. 

This map is of my hometown, so I’m more interested to see what database querying reveals, and I’d like an opportunity to contribute to its improvement on OpenStreetMap.org.

## 1. Data Audit

#### 1.1. Unique tags
For the first data audit task, '1\_unique\_tags.py' counts the unique tags.

Name | Count
------------ | -------------
node          | 1082390
nd              | 1395801
bounds      | 1
member      | 23781
tag              | 431569
relation        | 2196
way             | 174004
osm            | 1

**node**, **nd**, **member**, **tag**, **relation**, and **way** seem having resoanable number of counts. 

#### 1.2. Attributes types

So I checked the type of attribtues of those elements. 

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

Type of major nodes seems not including critical issue, as all nodes have unique attribute value except attribute **v** in tag element. However, it is not a problematic because tag elements hold various kind of values accordingly different keys. For example,

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

Above code has 8 different keys, **k**, in a tag element's attribute; **name, source, highway, alt_name, naptan:Street, naptan:Bearing, naptan:AtcoCode, naptan:Landmark**, and types of those keys' value are either strings or numbers.

#### 1.3. Key and value of tag attributes

To know whether the elements are meaningfule, in other words what kind of information in elements is the most dominant, I counted their children based on tag names.

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

<!--
	```Python
	<< node >>
	highway: 7767
	name: 6184
	source: 5742
	naptan:Street: 3800
	naptan:AtcoCode: 3793
	naptan:Landmark: 3771
	naptan:verified: 3760
	naptan:Indicator: 3749
	naptan:CommonName: 3742
	naptan:Bearing: 3729
	naptan:PlusbusZoneRef: 3660
	created_by: 2983
	amenity: 2408
	alt_name: 1739
	naptan:AltCommonName: 1684
	barrier: 1679
	addr:housenumber: 1575
	shop: 662
	power: 653
	crossing: 611
	addr:street: 562
	ref: 481
	ele: 438
	foot: 415
	traffic_calming: 405
	natural: 402
    bicycle: 342
	.
	.
	.
	
	<< relation >>
	type: 2111
	name: 1661
	source: 1514
	site: 1460
	naptan:verified: 1448
	naptan:StopAreaCode: 1445
	naptan:StopAreaType: 1443
	restriction: 206
	route: 169
	operator: 144
	ref: 141
	building: 80
	boundary: 49
	network: 41
	landuse: 40
	admin_level: 37
	natural: 29
	website: 24
	to: 20
	public_transport:version: 20
	from: 20
	wikidata: 16
	highway: 16
	amenity: 15
	addr:street: 15
	wikipedia: 13
	addr:postcode: 13
	service: 11
	except: 11
	designation: 11
	addr:housenumber: 10
	.
	.
	.
	
	<< way >>
	building: 112076
	source: 92744
	highway: 38054
	name: 20406
	landuse: 8769
	addr:housenumber: 4076
	barrier: 3709
	surface: 3569
	addr:street: 3099
	oneway: 2958
	natural: 2794
	maxspeed: 2784
	foot: 2728
	amenity: 2353
	service: 2180
	ref: 2023
	lit: 2011
	postal_code: 1577
	addr:postcode: 1469
	access: 1221
	railway: 1173
	leisure: 1145
	lanes: 1073
	addr:city: 1050
	layer: 923
	bridge: 910
	bicycle: 910
	shop: 889
	gauge: 855
	electrified: 803
	waterway: 785
	tracks: 683
	created_by: 668
	source:name: 627
	passenger: 567
	.
	.
	.
	```
-->
Interestingly, there were no additional tag children in **member** and **nd** elements, while **node**, **tag**, and **relation** have many additional information.

**node**, **relation**, and **way** elements contain children nodes called tag, but they are not included in **member** and **nd** elements. In other words, there are no additional information in **member** and **nd** elements, while **node**, **tag**, and **relation** have many additional information conceived in sub-nodes, tag. Thus, I only focus the further audit tasks on those three elements.

## 2. Problems Encountered in the Map Dataset

#### 2.1. Problems in street name
In Sheffield, there are many unique road types which go beyond the given basic types; *Street, Avenue, Boulevard, Drive, Court, Place, Square, Lane*, and *Road*, for example *Upperthorpe Glen*, and *Fargate*. So after I implemented a code (problematic\_street\_name.py) which tells about unique street names, in other world not be included in the given basic road type list, I searched the unique street names on Google map, and checked if they are really unique name or mistyped name.

- Place name and not a street name: 
	- Edmund Road Business Centre
	- Riverside Park Industrial Estate 
	- Sheaf Gardens Industrial Estate (also not in Sheffield)
	- Upperthorpe -> Upperthorpe road
	- Mount Pleasant Park -> Mount Pleasant Road
	- Archer Road Retail Park -> Archer Road
	- Victoria Villas -> Victoria Road or Victoria Street)
- Abbrebiation: 
	- Eccelsall rd
- Not in Sheffield: 
	- Waterthorpe Greenway is in Westfield
	- Sheaf Gardens Industrial Estate in Middlesbrough
	- Sheffield Digital Campus (no where)
- duplicated:
	- Barker's Pool and Barkers Pool
- Wrong name: 
	- Utah Terrace -> Utah Road
	- Westgate -> West Street
	- 462 -> 462 London road (not sure)
- Additional Road Type:
	- Green
	- North
	- Gardens
	- South
	- View
	- Parade
	- Walk
	- Row
- Unique Road Name:
	- Crookes
	- Backfields
	- Shalesmoor
	- Birkendale
	- The Crofts
	- Moorfields
	- Rutland Park

It problematic\_street\_name.py, I added two lists along side the given expected road name list. Road types which are used in Sheffield were added to the first list. Second list have unique road names of the place.

#### 

## Problems Encountered in the Map
After initially downloading a small sample size of the Charlotte area and running it against a provisional data.py file, I noticed five main problems with the data, which I will discuss in the following order:


- Over­abbreviated street names *(“S Tryon St Ste 105”)*
- Inconsistent postal codes *(“NC28226”, “28226­0783”, “28226”)*
- “Incorrect” postal codes (Charlotte area zip codes all begin with “282” however a large portion of all documented zip codes were outside this region.)
- Second­ level `“k”` tags with the value `"type"`(which overwrites the element’s previously processed `node[“type”]field`).
- Street names in second ­level `“k”` tags pulled from Tiger GPS data and divided into segments, in the following format:

	```XML
	<tag k="tiger:name_base" v="Stonewall"/> 
	<tag k="tiger:name_direction_prefix" v="W"/> 
	<tag k="tiger:name_type" v="St"/>
	```

### Over­abbreviated Street Names
Once the data was imported to SQL, some basic querying revealed street name abbreviations and postal code inconsistencies. To deal with correcting street names, I opted not use regular expressions, and instead iterated over each word in an address, correcting them to their respective mappings in audit.py using the following function:

```python 
def update(name, mapping): 
	words = name.split()
	for w in range(len(words)):
		if words[w] in mapping:
			if words[w­1].lower() not in ['suite', 'ste.', 'ste']: 
				# For example, don't update 'Suite E' to 'Suite East'
				words[w] = mapping[words[w]] name = " ".join(words)
	return name
```

This updated all substrings in problematic address strings, such that:
*“S Tryon St Ste 105”*
becomes:
*“South Tryon Street Suite 105”*

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
