from Cimpl import *




def weighted_grayscale(img):
    """ (Cimpl.Image) -> None
    
    Convert the specified picture into a grayscale image with improved results
    takes human perception into account
    
    >>> image = load_image(choose_file()) 
    >>> weighted_grayscale(image)
    >>> show(image)        
    """
    
    for pixel in img:
        x, y, col = pixel
        r, g, b = col

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness_red = r*0.299
        brightness_green = r*0.587
        brightness_blue = r*0.114
        total_brightness=( brightness_red+brightness_green+brightness_blue)
        gray = create_color( total_brightness, total_brightness, total_brightness)
        
        set_color(img, x, y, gray)
        
def solarize(img, threshold):
    """ (Cimpl.Image) -> None
    
    Solarize the specified image,modifying all RGB
    components with intensities that are less than the
    specified threshold.
    
    >>> image = load_image(choose_file()) 
    >>> solarize(image,128)
    >>> show(image)     
    """

    for x, y, col in img:
        red, green, blue = col

        # Invert the values of all RGB components that are less than threshold,
        # leaving components with higher values unchanged.

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        col = create_color(red, green, blue)
        set_color(img, x, y, col)
        
def black_and_white_and_gray(img):
    """ (Cimpl.Image) -> None
    
    Convert the specified image to a black-and-white-and-gray
    (three-shade) image.

    >>> image = load_image(choose_file()) 
    >>> black_and_white_and_gray(image)
    >>> show(image)     
    """

    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of
    # pixels whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, col in img:
        red, green, blue = col
        
        brightness = (red + green + blue) // 3

        if brightness < 85:
            set_color(img, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(img, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(img, x, y, white)
            
def extreme_contrast(img):
    """ (Cimpl.Image) -> none
    modify img, maximizing contrast between the light and dark pixels
    >>> image = load_image(choose_file()) 
    >>> extreme_contrast(image)
    >>> show(image)
    """
    for x, y, col in img:
        red,green,blue = col
        if red < 127:
            red = 0
        else:
            red = 255

        if green < 127:
            green = 0
        else:
            green = 255

        if blue < 127:
            blue = 0
        else:
            blue = 255

        col = create_color(red, green, blue)
        set_color(img, x, y, col)
        
def sepia_tint(img):
    """(Cimpl.Image)->None
    Convert the specified image to sepia tones.
    >>> image=load_image(choose_file())
    >>> sepia_tint(image)
    >>> show(image)
    """
    grayscale(img)
    for pixel in img:
        x,y,col = pixel
        red,green,blue = col
        if red<63:
            blue=blue*0.9
            red=red*1.1
        elif 63 <= red <= 191:
            blue=blue*0.85
            red=red*1.15
        else:
            blue=blue*0.93
            red=red*1.08
        col = create_color(red, green, blue)
        set_color(img, x, y, col)   
        
def blur(source):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of the image bound to source.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(original)
    show(blurred)    
    """

    # We modify a copy of the original image, because we don't want blurred
    # pixels to affect the blurring of subsequent pixels.
    
    target = copy(source)
    
    # Recall that the x coordinates of an image's pixels range from 0 to
    # get_width() - 1, inclusive, and the y coordinates range from 0 to
    # get_height() - 1.
    #
    # To blur the pixel at location (x, y), we use that pixel's RGB components,
    # as well as the components from the four neighbouring pixels located at
    # coordinates (x - 1, y), (x + 1, y), (x, y - 1) and (x, y + 1).
    #
    # As such, we can't use this loop to generate the x and y coordinates:
    #
    # for y in range(0, get_height(source)):
    #     for x in range(0, get_width(source)):
    #
    # With this loop, when x or y is 0, subtracting 1 from x or y yields -1, 
    # which is not a valid coordinate. Similarly, when x equals get_width() - 1 
    # or y equals get_height() - 1, adding 1 to x or y yields a coordinate that
    # is too large.
    #
    # We have to adjust the arguments passed to range to ensure that (x, y)
    # never specifies the location of pixel on the top, bottom, left or right 
    # edge of the image, because those pixels don't have four neighbours.
   
    for y in range(1, get_height(source) - 1):
        for x in range(1, get_width(source) - 1):
            total_red=0
            total_green=0
            total_blue=0            
            # Grab the pixel @(x, y) and its four neighbours
            for y2 in range(y-1,y+2):
                for x2 in range(x-1,x+2):
                    
                    r,g,b=get_color(source,x2,y2)
                    total_red=total_red+r
                    total_green=total_green+g
                    total_blue=total_blue+b


            # Average the red components of the five pixels
            new_red = (total_red ) // 9

            # Average the green components of the five pixels
            new_green = (total_green ) // 9

            # Average the blue components of the five pixels
            new_blue = (total_blue) // 9

            # Blur the pixel @(x, y) in the copy of the image
            new_color = create_color(new_red, new_green, new_blue)
            set_color(target, x, y, new_color)

    return target

def detect_edges_better(img,threshold):
    """(Cimpl.Image,float)->None
    Modify the specified image using edge detection.
    An edge is detected when a pixel's brightness differs
    from that of its neighbour by an amount that is greater
    then the specified threshold.
    >>>image=load_image(choose_file())
    >>>detect_edges_better(image,10.0)
    >>>show(image)
    """      
    
    for y in range(1, get_height(img) - 1):
        for x in range(1, get_width(img) - 1):
            
            top_r,top_g,top_b=get_color(img,x,y)
            bottom_r,bottom_g,bottom_b=get_color(img,x,y+1)
            right_r,right_g,right_b=get_color(img,x+1,y)
            
            contrast_top=(top_r+top_g+top_b)//3
            contrast_bottom=(bottom_r+bottom_g+bottom_b)//3
            contrast_right=(right_r+right_g+right_b)//3
            
            compare=abs(contrast_top-contrast_bottom)
            compare2=abs(contrast_top-contrast_right)
            
            if compare > threshold or compare2 > threshold:
                col=create_color(0,0,0)
                set_color(img, x,y,col)
            else:
                col=create_color(255,255,255)
                set_color(img, x,y,col)
                
def negative(img):
    
    """ (Cimpl.Image) -> None
      
      Convert the specified picture into a negative image.
      
      >>> image = load_image(choose_file()) 
      >>> negative(image)
      >>> show(image)        
      """
    for pixel in img:
        x, y, col = pixel
        r, g, b = col
        r = 255-r
        g = 255-g
        b = 255-b
        col = create_color(r, g, b)
        set_color(img, x, y, col)
        
