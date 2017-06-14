# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 19:49:35 2017

@author: lab
"""

#用r（c，s）评估分层聚类的好坏

from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

X = [[0, 1.3, 1.0, 1.0, 1.3, 1.3, 0.7],
     [1.3, 0, 1.2, 1.2, 0.1, 0.4, 1.3],
     [1.0, 1.2, 0, 0.5, 1.3, 1.2, 1.0],
     [1.0, 1.2, 0.5, 0, 1.3, 1.3, 1.0],
     [1.3, 0.1, 1.3, 1.3, 0, 0.2, 1.2],
     [1.3, 0.4, 1.2, 1.3, 0.2, 0, 1.2],
     [0.7, 1.3, 1.0, 1.0, 1.2, 1.2, 0]]

C = linkage(X, 'single')

print pdist(X)

c, coph_dists = cophenet(C, pdist(X))

print coph_dists

print c
