#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

import dlib
from skimage import io
import cv2

from dip import selective_search


parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

image_file = args.filename
img = io.imread(image_file)
# Locations of candidate objects will be saved into rects
rects = []
dlib.find_candidate_object_locations(
    img,
    rects,
    kvals=(50, 200, 3),
    min_size=20,
    max_merging_iterations=50,
    )

dst = selective_search.draw_rects(img, rects)
decomposed = selective_search.decompose(img, rects, num=3)

for img in [dst] + decomposed:
    io.imshow(img)
    io.show()
