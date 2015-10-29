#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from skimage.io import imread
from sklearn.datasets import load_files


_this_dir = os.path.dirname(os.path.abspath(__file__))


def load_raw_images():
    container_path = os.path.join(_this_dir, '../data/raw_image')
    dataset = load_files(container_path=container_path, load_content=False)
    return dataset


def load_mask_images():
    container_path = os.path.join(_this_dir, '../data/mask_image')
    dataset = load_files(container_path=container_path, load_content=False)
    return dataset


def load_image_files(files):
    for f in files:
        yield imread(f)
