# Active_Contours

## Segmentation Instructions
**Necessary Installations**
 * **skimage** using `pip install scikit-image` or `conda install -c conda-forge scikit-image`.
 * **numpy**
 * **matplotlib**

Make sure both **find_segments.py** and **your program(find_segments_ex.py)** are in the same directory. Run the find_segment_ex.py program, which uses a sample image from skimage.data.

## Sample Image
**Input Image**

![Input_Image](https://github.com/MadhavanTR/Active_Contours/blob/master/sample.png)

**Output with segments**

![Output_Image](https://github.com/MadhavanTR/Active_Contours/blob/master/output.png)

 Time consumed to identify snakes/contours is caculated with

```
st = time.time()
output_snakes = find_segments(image_gray, 4, centers, radii)
print(time.time()-st)
```

and the result was

`4.892950057983398`

and this time linearly increases with number of segments identified.
