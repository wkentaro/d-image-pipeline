#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import cPickle as pickle

import numpy as np

from dip.load_data import (
    load_raw_images,
    load_mask_images,
    load_image_files,
)
from dip.mask import convert_masks_to_target


_this_dir = os.path.dirname(os.path.abspath(__file__))
_IMAGE_SHAPE = (712, 1068)


def get_dataset():
    cache_file = os.path.join(_this_dir, '../tmp_data/dataset.pkl.gz')
    if os.path.exists(cache_file):
        with open(cache_file, 'rb') as f:
            dataset = pickle.load(f)
        return dataset['data'], dataset['target']

    raw_dataset = load_raw_images()
    data = load_image_files(raw_dataset.filenames)
    data = np.array(list(data))

    mask_dataset = load_mask_images()
    masks = load_image_files(mask_dataset.filenames)
    target = convert_masks_to_target(masks, negative=True)

    with open(cache_file, 'wb') as f:
        dataset = {'data': data, 'target': target}
        pickle.dump(dataset, f)

    return data, target


X, y = get_dataset()
