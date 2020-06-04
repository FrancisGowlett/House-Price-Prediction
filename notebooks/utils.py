import os
import pandas as pd
import numpy as np
import pathlib
import tarfile
from six.moves import urllib


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"
HOUSING_PATH = pathlib.Path.cwd()
HOUSING_PATH = os.path.join(HOUSING_PATH.parent, "data")


# Download housing data file and extract it
# urllib.request gets url data, .urlretrieve puts data into a file
def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


# Return csv data as df
def load_housing_data(housing_path):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)
    
    
# Takes 2 Series = 'attribute being compared' : 'proportion'
# Returns df of comparisons
def check_split_proportions(overall, sample):
    overall.sort_index(inplace=True)
    sample.sort_index(inplace=True)
    proportions_split_against_original = pd.DataFrame({'Overall': overall,
                                                'Stratified': sample})
    return proportions_split_against_original.head()
