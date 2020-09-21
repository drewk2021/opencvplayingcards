import load_display
import imutils
import cv2

# implementing Chapter 3: Loading and Displaying
baseCardPath = load_display.getCardFromUser()
baseCardImage = cv2.imread(baseCardPath)
load_display.display(imutils.resize(baseCardImage,width=500),"base-resized")
