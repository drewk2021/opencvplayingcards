import cv2
import numpy as np
import argparse
import imutils
import blur


def cannify(image, thres1 = 30, thres2 = 150):
    """
    Purpose: To impose the cv2.Canny() function on an image, which subjects it to
    Sobel gradients in both dimensions and identifies "edge-like" regions.
    Parameters: An image (numpy array), an arbitrary threshold value for which
    lesser gradients will not be considered edges (int) defaulted at 30, and an
    arbitrary threshold value for which greater gradients will be considered edges
    (int) defaulted at 150, with gradient values in between then identified as
    "edge-like" or not by the cv2.Canny() function.
    Return: A cannied image (numpy array).
    """
    # converting image from BGR to greyscale; no information is contained in the card's color
    # from a supervised perspective
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gblurred = blur.gBlur(image) # gaussian blur with default parameters

    cannied = cv2.Canny(gblurred, thres1, thres2)
    return cannied




if __name__ == '__main__':
    ap = argparse.ArgumentParser() # constructing ArgumentParser() object
    ap.add_argument("-1","--image",required=True,help="input path to image file")
    args = vars(ap.parse_args())

    card = cv2.imread(args["image"])
    canniedCard = cannify(imutils.resize(card,height=300))
    cv2.imshow("cannied", canniedCard)
