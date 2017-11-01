#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL", 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below
''' Not wroking, but good example to sort zipped_data using multiple values.
names = data_dict.keys()
#print names
zipped_data = zip(names, data)
print len(names), len(data)
sort1 = sorted(zipped_data, key = lambda x: (x[1][0], x[1][1]), reverse = True)[:2]
#sort2 = sorted(sort1, key = lambda x: x[1][1], reverse = True)[:2]
print sort1
'''
two_outliers = []
for key, value in data_dict.iteritems():
    if (value["salary"] > 10**6 and value["salary"] != "NaN") and (value["bonus"] > 5*10**6 and value["bonus"] != "NaN"):
        print key, value["salary"], value["bonus"]
'''
### Visualisation
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
    if 

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
'''
