# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:25:53 2019

@author: trrsm

Example using find_segments.py
"""
from find_segments import find_segments
import skimage.data as data
import skimage.color as color
import matplotlib.pyplot as plt

image = data.astronaut()
image_gray = color.rgb2gray(image) 

#From the object identifier we must get these datas: centers and radii
centers = [[100, 230], [160, 400], [390, 170], [450, 380]]
radii = [[90], [90], [40], [130]]

output_snakes = find_segments(image_gray, 4, centers, radii)

fig, ax = plt.subplots(1, 1)
ax.imshow(image, cmap='gray')
ax.axis('off')
for i in range(4):
    ax.plot(output_snakes[i, :, 0], output_snakes[i, :, 1], '-b', lw=3);