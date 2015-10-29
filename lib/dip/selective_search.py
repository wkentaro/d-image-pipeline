#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cv2


def draw_rects(src, rects):
    dst = src.copy()
    for rect in rects:
        min_x, min_y = rect.left(), rect.top()
        max_x, max_y = rect.right(), rect.bottom()
        cv2.rectangle(dst, (min_x, min_y), (max_x, max_y), color=(255, 0, 0))
    return dst
