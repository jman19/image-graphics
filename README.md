# Image-graphics

Created for university lab assigments. The functions uses cimpl in order to get the rgb components in each pixel by giving cimpl the specific pixel's coordinates. 

The rgb values are then manipulated by the diffrent function's algorithms, for example the gray scale filter calculates the gradiant of gray by averaging the intensity of the rgb values and then setting each of the rgb values to that calculated intensity to create the shade of gray for that pixal.

contains functions used in image processing and module named cimpl Cimpl (Carleton Image Manipulation Python Library).

Copyright (c) 2013 - 2014, D.L. Bailey,
Department of Systems and Computer Engineering,
Carleton University

## Requirements
works with python 3.4.3 and pillow 2.9.0

## Example
How to run
```
>>> image = load_image(choose_file()) 
>>> weighted_grayscale(image)
>>> show(image) 
```

created using `def weighted_grayscale(img):` found in filter.py
![Imgur](http://i.imgur.com/UthAITh.png)
