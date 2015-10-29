#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def bounding_rect_of_mask(mask, negative=False):
    if negative:
        mask = ~mask
    where = np.argwhere(mask)
    (y_start, x_start), (y_end, x_end) = where.min(0), where.max(0) + 1
    return [x_start, x_end, y_start, y_end]


def convert_masks_to_target(masks, negative=False):
    target = []
    for mask in masks:
        target.append(bounding_rect_of_mask(mask, negative=negative))
    return np.array(target)
