import load_display
import imutils
import construct_histogram
import cv2

# implementing Chapter 3: Loading and Displaying, and Chapter 6: Image Processing
baseCardPath = load_display.getCardFromUser()
baseCardImage = cv2.imread(baseCardPath)
load_display.display(imutils.resize(baseCardImage,width=500),"base-resized") # resizing proportionally to width of 500 pixels



# implementing Chapter 7: Histograms
print("\nLet's visualize our pixel distributions!\n")
construct_histogram.histogram3D(baseCardImage) # using default parameters
