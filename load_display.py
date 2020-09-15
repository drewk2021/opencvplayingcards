import cv2
import argparse

# testing out jpg input
ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required=True,help="input path to image file")
args = vars(ap.parse_args())

def display(imagePath, moveOn = False):
    # imagePath str, boolean defaulted to staying at image
    image = cv2.imread(imagePath)
    cv2.imshow(imagePath, image)
    if not moveOn:
        cv2.waitKey(0) # move on with any key input

# loading image with cv2
display(args["image"])
