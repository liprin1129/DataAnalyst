#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

## What's the number of features in your data? (Hint: the data is organized
## into a numpy array where the number of rows is the number of data points
## and the number of columns is the number of features; so to extract this number,
## use a line of code like len(features_train[0]).)
print len(features_train[0])

#########################################################


