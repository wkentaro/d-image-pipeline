#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import time

import skimage.io as io
from skimage.transform import resize

from dip import load_raw_images, load_mask_images


parser = argparse.ArgumentParser()
parser.add_argument('shape_0', type=int)
parser.add_argument('shape_1', type=int)
args = parser.parse_args()

shape = (args.shape_0, args.shape_1)

raw_dataset = load_raw_images()
for i, f in enumerate(raw_dataset.filenames):
    print(f)
    img = io.imread(f)
    if i == 0:
        print('resize: {0} -> {1}'.format(img.shape[:2], shape))
    resized = resize(img, output_shape=shape)
    io.imsave(f, resized)


mask_dataset = load_mask_images()
for i, f in enumerate(mask_dataset.filenames):
    print(f)
    img = io.imread(f)
    if i == 0:
        print('resize: {0} -> {1}'.format(img.shape[:2], shape))
    resized = resize(img, output_shape=shape)
    io.imsave(f, resized)
