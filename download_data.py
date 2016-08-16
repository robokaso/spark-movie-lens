#! /usr/bin/env python

import os
import urllib
import zipfile

datasets_path = os.path.join('.', 'datasets')
if not os.path.exists(datasets_path):
    os.makedirs(datasets_path)

small_dataset_url = 'http://files.grouplens.org/datasets/movielens/ml-latest-small.zip'
small_dataset_path = os.path.join(datasets_path, 'ml-latest-small.zip')

small_f = urllib.urlretrieve (small_dataset_url, small_dataset_path)

with zipfile.ZipFile(small_dataset_path, "r") as z:
    z.extractall(datasets_path)


