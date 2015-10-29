#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@param X: input image
@param y: selective search parameter
    - [kval_0=50, kval_1=200, kval_2=3, min_size=20, max_merging_iterations=50]
    - n_param: 5
"""

import sys
import logging

logging.basicConfig(
            format="%(message)s",
            level=logging.DEBUG,
            stream=sys.stdout)

import cPickle as pickle
import gzip
import os

import numpy as np
from sknn import ae, mlp
from sklearn.preprocessing import normalize
from sklearn.cross_validation import train_test_split
from skimage.transform import resize

from dip.load_data import load_raw_images, load_image_files


datasets = load_raw_images()

filenames = datasets.filenames

filenames_train, filenames_test = train_test_split(filenames)

batch_size = 30

N = len(filenames)
n_param = 5
n_iter = 10


myae = ae.AutoEncoder(
            layers=[
                ae.Layer('Tanh', units=128),
                ae.Layer('Sigmoid', units=64),
            ],
            learning_rate=0.002,
            n_iter=10,
        )


for _ in xrange(n_iter):
    print '--------------------------------------------------------'
    p = np.random.randint(0, N, batch_size)
    images = load_image_files(filenames[p], as_grey=True)
    X = np.array([resize(im, (356,534)).reshape(-1) for im in images])
    y = np.zeros((batch_size, n_param), dtype=np.float)

    print 'X:\n{0}\n{1}'.format(X, X.shape)
    print 'y:\n{0}\n{1}'.format(y, y.shape)

    X = X.astype(np.float) / 255.

    print 'X: \n{0}\n{1}'.format(X, X.shape)

    myae.fit(X)

    print 'dir(myae):\n{0}'.format(dir(myae))
    print 'myae.__dict__:\n{0}'.format(myae.__dict__)
    print '--------------------------------------------------------'

mymlp = mlp.Regressor(
            layers=[
                mlp.Layer('Tanh', units=128),
                mlp.Layer('Sigmoid', units=64),
                mlp.Layer('Linear'),
            ],
        )

myae.transfer(mymlp)
mymlp.fit(X, y)


mymlp.predict(X_test)