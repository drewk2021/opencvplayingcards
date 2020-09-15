import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required=True,help="input path to image file")
args = vars(ap.parse_args())

card = cv2.imread(args["image"])


def cannify(image, moveOn = False):

    # converting image from BGR to greyscale; no information is contained in the card's color
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gblurred = cv2.GaussianBlur(image,(5,5),0) # gaussian blur with 5 by 5 kernel

    cannied = cv2.Canny(gblurred, 30, 150)
    cv2.imshow("cannied", cannied)

    if not moveOn:
        cv2.waitKey(0)


cannify(card)
