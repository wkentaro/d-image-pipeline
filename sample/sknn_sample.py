#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split

from sknn.mlp import Classifier, Layer

dataset = load_iris()

X = dataset.data
y = dataset.target

X_train, X_valid, y_train, y_valid = train_test_split(X, y)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train)

nn = Classifier(
    layers=[
        Layer("Rectifier", units=100),
        Layer("Linear")],
    learning_rate=0.02,
    n_iter=10)
nn.fit(X_train, y_train)

y_valid = nn.predict(X_valid)

score = nn.score(X_test, y_test)

print(score)
