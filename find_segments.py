# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:00:12 2019

@author: trrsm

Function to identify contours using existing active_contour function
"""
import numpy as np
import skimage.segmentation as seg
import skimage.color as color

def find_segments(image, n, centers, radius):
    image_gray = color.rgb2gray(image) 
    
    #Using a resolution of 199, or number of points on the snake as 199
    snakes = np.zeros(shape=(n, 199, 2))    
    circles = np.zeros(shape=(n, 199, 2))
    cp = np.zeros(shape=(200, 2))    
    
    # to save intermediate or temp values
    for i in range(n):
        radians = np.linspace(0, 2*np.pi, 200)
        c = centers[i][1] + radius[i]*np.cos(radians)
        r = centers[i][0] + radius[i]*np.sin(radians)
        cp = np.array([c, r]).T
        circles[i] = cp[:-1]
        
        #   With circular boundary, narrow down to the contour
        snakes[i] = seg.active_contour(image_gray, circles[i], alpha=0.05, beta=0.5)

    return snakes