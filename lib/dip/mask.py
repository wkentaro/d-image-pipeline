#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def bounding_rect_of_mask(mask, negative=False):
    """
    @returns (min_x, max_x, min_y, max_y)
    """
    if negative:
        mask = ~mask
    where = np.argwhere(mask)
    (y_start, x_start), (y_end, x_end) = where.min(0), where.max(0) + 1
    return (x_start, x_end, y_start, y_end)
