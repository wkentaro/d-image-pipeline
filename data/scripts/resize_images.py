#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import time

import skimage.io as io
from skimage.transform import resize

from dip.load_data import load_raw_images, load_mask_images


parser = argparse.ArgumentParser()
parser.add_argument('--shape0', type=int, default=1424)
parser.add_argument('--shape1', type=int, default=2136)
args = parser.parse_args()

shape = (args.shape0, args.shape1)

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
