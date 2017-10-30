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

## Question 13
print 'Q13. No. of dataset:', len(enron_data)

## Question 14
print 'Q14. No. of features:', len(enron_data['METTS MARK'])

## Question 15
interest_people = 0
for iter_dict in enron_data.iteritems():
    if iter_dict[1]['poi'] == True:
        interest_people += 1
    #print iter_dict

print 'Q15. No. of people of interest', interest_people

## Question 16
with open('../final_project/poi_names.txt', 'r') as fp:
    count = 0
    for line in fp.readlines():
        if line.startswith('('):
            count += 1
        #count += 1
    print 'Q16. No. of people of interest in poi_names.txt:', count

## Question 18
print 'Q18. Total stck value belonging to James Prentice:', enron_data['PRENTICE JAMES']['total_stock_value']
'''
for data in enron_data.iteritems():
    if 'JAMES' in data[0]:
        print data[0]
    #print data[0]
'''

## Question 19
answer = enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print 'Q19. No. of email messages from Wesley Colwell to persons of interest:', answer

## Question 20
answer = enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print 'Q20. The value of stock options exercised by Jeffrey K Skilling:', answer

## Question 25
import numpy as np
Fastow = enron_data['FASTOW ANDREW S']
Skilling = enron_data['SKILLING JEFFREY K']
Lay = enron_data['LAY KENNETH L']
print 'Maximum total payments:', np.argmax([Fastow['total_payments'], Skilling['total_payments'], Lay['total_payments']])
print 'Maximum total payments:',Lay['total_payments']
'''
for data in enron_data.iteritems():
    if 'KENNETH' in data[0]:
        print data[0]
'''

## Question 27
count = 0
count1 = 0
for iter_dict in enron_data.iteritems():
    if iter_dict[1]['salary'] != 'NaN':
        #print iter_dict[1]['salary']
        count += 1
    if iter_dict[1]['email_address'] != 'NaN':
        #print iter_dict[1]['email_address']
        count1 += 1
        
print 'Q27. No. of folks having quantified salary:', count
print 'Q27. No. of folks having email address:', count1

## Question 29
count = 0
for iter_dict in enron_data.iteritems():
    if iter_dict[1]['total_payments'] == 'NaN':
        count += 1

print "Q29. No. of people having 'NaN' for their total payments:", count
print "Q29. Percentage of people having 'NaN' for their total payments:", count / float(len(enron_data)) * 100

## Question 30
count = 0
for iter_dict in enron_data.iteritems():
    #if iter_dict[1]['total_payments'] == 'NaN' and iter_dict[1]['poi'] == True:
    if iter_dict[1]['poi'] == True:
        count += 1

print "Q30. No. of people having 'NaN' for their total payments:", count
print "Q30. Percentage of people having 'NaN' for their total payments:", count / float(len(enron_data)) * 100

## Question 31
print len(enron_data)
