import load_display
import imutils
import construct_histogram
import blur
from cannify import cannify
import findCard
import numpy as np
import cv2

# implementing Chapter 3: Loading and Displaying, and Chapter 6: Image Processing
baseCardPath = load_display.getCardFromUser()
baseCardImage = cv2.imread(baseCardPath)
card = baseCardImage.copy() # ref variable
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



# implementing Chapter 10: Gradients and Edge Detection
print("\nWhere are our meaningful edges?\n")
cannyCard = cannify(baseCardImage) # using default parameters
load_display.display(imutils.resize(cannyCard, width=500),"Greyscale canny")


# implementing Chapter 11: Contours, Chapter 4: Image Basics, and Chapter 5: Drawing
print("\nLet's isolate the card!\n")
croppedCard = findCard.getCardFromImage(card)
load_display.display(imutils.resize(croppedCard, width=500), "Focused on Card")
