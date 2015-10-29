#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cv2
import numpy as np


def draw_rects(src, rects):
    dst = src.copy()
    for rect in rects:
        min_x, min_y = rect.left(), rect.top()
        max_x, max_y = rect.right(), rect.bottom()
        cv2.rectangle(dst, (min_x, min_y), (max_x, max_y), color=(255, 0, 0))
    return dst


def decompose(src, rects, num=3):
    p = np.random.randint(0, len(rects), 3)
    cropped_list = []
    for i in p:
        rect = rects[i]
        min_x, min_y = rect.left(), rect.top()
        max_x, max_y = rect.right(), rect.bottom()
        cropped = src[min_y:max_y, min_x:max_x]
        cropped_list.append(cropped)
    return cropped_list
