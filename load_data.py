# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:25:33 2018

@author: CrystalGlacier
"""
import scipy as sp

def load_data(data_dir):
    dirs = [d for d in os.listdir(data_dir)
        if os.path.isdir(os.path.join(data_dir, d))]
    labels = []
    images = []
    for d in dirs:
        label_dir = os.path.join(data_dir, d)
        file_names = [os.path.join(label_dir, f)
            for f in os.listdir(label_dir)
            if f.endswith(".ppm")]
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append(int(d))
    return images, labels
            