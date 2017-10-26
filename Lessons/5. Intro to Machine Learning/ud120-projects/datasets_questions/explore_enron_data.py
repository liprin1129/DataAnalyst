#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print 'Q13: No. of dataset:', len(enron_data)
print 'Q14: No. of features:', len(enron_data['METTS MARK'])

interest_people = 0
for iter_dict in enron_data.iteritems():
    if iter_dict[1]['poi'] == True:
        interest_people += 1
    #print iter_dict

print 'Q15: No. of people of interest', interest_people
