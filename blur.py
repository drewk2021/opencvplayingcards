import cv2
import numpy as np
import argparse


def gBlur(image, kernel = 11):
    """
    Purpose: To implement a gaussian blur on an image.
    Parameters: An image (numpy array), a kernel side length (int) defaulted to 11 and
    must be an odd number for convolution.
    Return: A blurred image (numpy array).
    """

    # gaussian blurring performs an effective weighted average over a 2D kernel in the image.
    blurred = cv2.GaussianBlur(image, (kernel,kernel), 0) # 0 value instructs cv2 to compute std over x
    return blurred


def bilateralBlur(image, diameter = 9, colorSTD = 41, pixelSTD = 41):
    """
    Purpose: To implement a bilateral blur on an image, which retains edges while
    reducing noise.
    Parameters: An image (numpy array), a diameter of the local pixel area
    for gaussian weighting (int) defaulted to 7, a color std defining the distribution
    of colors for gaussian weighting (int) defaulted to 31, and a space std
    defining the disribution of pixels for gaussian weighting (int), defaulted
    to 31.
    Return: An image having undergon bilateral blurring (numpy array).
    """

    # biltateral blurring evaluates two gaussian functions:
    # 1) over the pixel space
    # 2) over the pixel intensity space
    blurred = cv2.bilateralFilter(image, diameter, colorSTD, pixelSTD)
    return blurred



if __name__ == '__main__':
    ap = argparse.ArgumentParser() # constructing ArgumentParser object
    ap.add_argument("-1","--image",required=True,help="input file path")
    args = vars(ap.parse_args())

    gblurred = gBlur(args["image"])
    cv2.imshow("Gaussian Blur",gblurred)
    cv2.waitKey(0)
