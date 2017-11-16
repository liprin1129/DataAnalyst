#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

pred = clf.predict(features)
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels)

print "Accuracy before seperating test set: ", acc

#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

new_clf = tree.DecisionTreeClassifier()
new_clf = new_clf.fit(X_train, y_train)

new_pred = new_clf.predict(X_test)

new_acc = accuracy_score(new_pred, y_test)
print "Accuracy after seperating test set:", new_acc

print "\nQ) How many POIs are predicted for the test set for your POI identifier?"
poi_n = sum(np.array(y_test) == 1)
print "\t=> {0} \n".format(sum(np.array(y_test) == 1))

print "Q) How many people total are in your test set?"
tot = len(y_test)
print "\t=> {0} \n".format(len(y_test))

print "Q) If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?"
print "\t=> {0} \n".format( (tot-poi_n)/float(tot))

print "Q) Look at the predictions of your model and compare them to the true test labels. Do you get any true positives? (In this case, we define a true positive as a case where both the actual label and the predicted label are 1)"
print "\t=> {0} \n".format( np.sum((pred == 1) == (np.array(y_test) == 1)) )

print "Q) As you may now see, having imbalanced classes like we have in the Enron dataset (many more non-POIs than POIs) introduces some special challenges, namely that you can just guess the more common class label for every point, not a very insightful strategy, and still get pretty good accuracy!\n\n"
print "Precision and recall can help illuminate your performance better. Use the precision_score and recall_score available in sklearn.metrics to compute those quantities. \n\nWhat's the precision?\n"

print "What's the recall? \n\n(Note: you may see a message like UserWarning: The precision and recall are equal to zero for some labels. Just like the message says, there can be problems in computing other metrics (like the F1 score) when precision and/or recall are zero, and it wants to warn you when that happens.)\n\nObviously this isn't a very optimized machine learning strategy (we haven't tried any algorithms besides the decision tree, or tuned any parameters, or done any feature selection), and now seeing the precision and recall should make that much more apparent than the accuracy did.\n"

from sklearn.metrics import confusion_matrix
print "\t=> confusion matrix: \n{0}".format(confusion_matrix(y_test, new_pred))

from sklearn.metrics import classification_report
print "\t=> precision and recall score: \n{0}".format(classification_report(y_test, new_pred))

print "In the final project you'll work on optimizing your POI identifier, using many of the tools learned in this course. Hopefully one result will be that your precision and/or recall will go up, but then you'll have to be able to interpret them. \nnHere are some made-up predictions and true labels for a hypothetical test set; fill in the following boxes to practice identifying true positives, false positives, true negatives, and false negatives. Let's use the convention that '1' signifies a positive result, and '0' a negative. \n\n\tpredictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]\n\n\ttrue labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]\n\nHow many true positives are there?"

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

print "\t=> {0}\n\n".format(6)

print "Suppose our data looks like this: \n\n\tpredictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]\n\ttrue labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]\n\n(this is fabricated data, just to give you some practice)\n\nHow many true negatives are there in this example?\n"
print "\t=> {0}\n\n".format(9)

print "How many false positives are there?"
print "\t=> {0}\n\n".format(3)

print "How many false negatives are there?\n\n"
print "\t=> {0}\n\n".format(2)

print "What's the precision of this classifier?\n\n"
print "\t=> {0}\n\n".format( 6./ (6+3))

print "What's the recall of this classifier?\n\n"
print "\t=> {0}\n\n".format( 6./ (6+2))

predictions = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print "predictions: ", predictions
print "true_labels: ", true_labels
print "\t=> precision and recall score: \n{0}\n\n".format(classification_report(true_labels, predictions))

predictions = [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print "predictions: ", predictions
print "true_labels: ", true_labels
print "\t=> precision and recall score: \n{0}\n\n".format(classification_report(true_labels, predictions))

predictions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print "predictions: ", predictions
print "true_labels: ", true_labels
print "\t=> precision and recall score: \n{0}\n\n".format(classification_report(true_labels, predictions))

predictions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print "predictions: ", predictions
print "true_labels: ", true_labels
print "\t=> precision and recall score: \n{0}\n\n".format(classification_report(true_labels, predictions))
