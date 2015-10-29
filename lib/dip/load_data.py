#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from skimage.io import imread
from sklearn.datasets import load_files

from .path import *


def load_raw_images():
    container_path = os.path.join(DATA_DIR, 'raw_image')
    dataset = load_files(container_path=container_path, load_content=False)
    return dataset


def load_mask_images():
    container_path = os.path.join(DATA_DIR, 'mask_image')
    dataset = load_files(container_path=container_path, load_content=False)
    return dataset


def load_image_files(files, as_grey=False):
    for f in files:
        yield imread(f, as_grey=as_grey)


def load_rests():
    data_path = os.path.join(DATA_DIR, 'rects.pkl.gz')
    if not os.path.exists(data_path):
        print("'rects.pkl.gz' does not exist")
        quit()
    with gzip.open(data_path, 'rb') as f:
        return pickle.load(f)
