import load_display
import imutils
import construct_histogram
import blur
import numpy as np
import cv2

# implementing Chapter 3: Loading and Displaying, and Chapter 6: Image Processing
baseCardPath = load_display.getCardFromUser()
baseCardImage = cv2.imread(baseCardPath)
load_display.display(imutils.resize(baseCardImage,width=500),"base-resized") # resizing proportionally to width of 500 pixels



# implementing Chapter 7: Histograms
print("\nLet's visualize our pixel distributions! When done, close the Figure\
 and click any key on base-resized. \n")
construct_histogram.histogram3D(baseCardImage) # using default parameters


# implementing Chapter 8: Blurring
print("\nHow can we reduce the noise?\n")
blurs = np.hstack([ #numpy.hstack() allows displaying together
    imutils.resize(baseCardImage,width=500),
    imutils.resize(blur.gBlur(baseCardImage),width=500), # using default parameters
    imutils.resize(blur.bilateralBlur(baseCardImage),width=500)]) # using default parameters
load_display.display(blurs,"See the basic image, a gaussian blur, and a bilateral blur.")
