#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import collections
import cPickle as pickle
from future_builtins import zip
import gzip

import numpy as np
from skimage import io
from sklearn.datasets.base import Bunch

from dip.load_data import load_image_files, load_mask_images
from dip.mask import bounding_rect_of_mask


datasets = load_mask_images()

data = []
for f, mask in zip(
        datasets.filenames,
        load_image_files(datasets.filenames),
        ):
    # rect: (min_x, max_x, min_y, max_x)
    rect = bounding_rect_of_mask(mask, negative=True)
    data.append(list(rect))
    print('{0}: {1}'.format(f, rect))

bunch = Bunch(name='mask rects')
bunch.data = np.array(data)
bunch.filenames = datasets.filenames
bunch.target = datasets.target
bunch.target_names = datasets.target_names
bunch.description = 'mask rects: (min_x, min_y, max_x, max_y)'

with gzip.open('rects.pkl.gz', 'wb') as f:
    pickle.dump(bunch, f)
