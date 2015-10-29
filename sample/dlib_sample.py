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
dlib.find_candidate_object_locations(img, rects, min_size=1000)

dst = selective_search.draw_rects(img, rects)

io.imshow(dst)
io.show()
