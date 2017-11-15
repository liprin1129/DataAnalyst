#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

pred = clf.predict(features)
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels)

print "Accuracy before seperating test set: ", acc

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

new_clf = tree.DecisionTreeClassifier()
new_clf = new_clf.fit(X_train, y_train)

new_pred = new_clf.predict(X_test)

new_acc = accuracy_score(new_pred, y_test)
print "Accuracy after seperating test set:", new_acc