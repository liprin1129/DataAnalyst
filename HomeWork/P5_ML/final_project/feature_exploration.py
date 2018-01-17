import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
import pandas as pd

fpm = "final_project_dataset_modified.pkl" 
fp = "final_project_dataset.pkl"

fpm_df = pickle.load( open(fpm, "r"))
fp_df = pickle.load( open(fp, "r") )

### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
fpm_df = pd.DataFrame(fpm_df)
fp_df = pd.DataFrame(fp_df)
#print type(fpm_df), type(fp_df)
print fpm_df.head()
features_list = ['poi','salary'] # You will need to use more features