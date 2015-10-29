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


def load_image_files(files):
    for f in files:
        yield imread(f)
