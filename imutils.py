import numpy as np
import cv2

def translate(image, deltax, deltay):
    Mtx = np.float32([[1,0, deltax],[0,1,deltay]]) # final value in each row corresponds to x,y translation respectively
    shifted = cv2.warpAffine(image, Mtx, (image.shape[1], image.shape[0])) # (width, height)
    return shifted



def rotate(image, angle, centerOfRotation = None, scale = 1.0):

    height, width = image.shape[0], image.shape[1]

    if centerOfRotation == None: # only if user doesn't supply an alternate center
        centerOfRotation = (width // 2, height // 2)


    Mtx = cv2.getRotationMatrix2D(centerOfRotation, angle, scale) # tuple center point, angle in degrees, and float scale factor
    rotated = cv2.warpAffine(image, Mtx, (width, height))
    return rotated



def resize(image, inter = cv2.INTER_AREA, width = None, height = None):

    previousHeight, previousWidth = image.shape[0], image.shape[1]
    newDimensions = None

    if width: # user-supplied new width
        ratio = width / previousWidth
        newDimensions = (width, int(ratio * previousHeight))

    elif height: # user-supplied new height
        ratio = height / previousHeight
        newDimensions = (int(ratio * previousWidth), height)

    else: # no user-supplied resize
        return Image


    resized = cv2.resize(image, newDimensions, inter) # (width,height) tuple, method of resizing
    return resized
