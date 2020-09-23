import cv2
from cannify import cannify
import imutils
import argparse
import numpy as np

def getCardFromImage(image):
    """
    Purpose: To isolate the playing card in the image with contours.
    Parameters: An image with a playing card and background (numpy array).
    Return: A cropped image of the card (numpy array).
    """

    cardEdges = cannify(image) # using default threshold parameters

    (cardContours, _) = cv2.findContours(cardEdges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # destructive to cardEdges

    card = image.copy() # storing numpy array in separate reference variable
    # drawing last contour in hierarchy onto base image; USUALLY captures meaningful outermost edges.
    cv2.drawContours(card,cardContours,len(cardContours)-1,(0,255,0),10)

    """
    FOR VERIFICATION BY REDUNDANCY, because cardContours[-1] may not represent the edges of the card.
    """
    minX,minY,maxX,maxY = card.shape[1], card.shape[0], 0, 0  # all pixels are between these values
    for cardContour in cardContours:
        y, x, height, width = cv2.boundingRect(cardContour) # sets minimum-area rectangle encasing the contour

        if x < minX:
            minX = x
        if y < minY:
            minY = y
        if (x+width) > maxX:
            maxX = x + width
        if (y+height) > maxY:
            maxY = y + height


    """
    # through masking
    mask = np.zeros(image.shape[:2], dtype = "uint8")
    cv2.rectangle(mask, (minX,minY), (maxX,maxY), 255, -1)
    masked = cv2.bitwise_and(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY), cv2.cvtColor(image,cv2.COLOR_BGR2GRAY), mask)
    return masked
    """

    crop = card[minX:maxX,minY:maxY]
    return crop

    """
    # This solution is more precise, but incorrect if there are small contours outside the card.

    # the last contour in the hierarchy captures the card's outermost edges, again.
    minY, minX, height, width = cv2.boundingRect(cardContours[len(cardContours)-1]) # sets minimum-area rectangle encasing the contour

    crop = card[minX: minX + width, minY: minY + height]
    return crop
    """


if __name__ == '__main__':
    ap = argparse.ArgumentParser() # constructing ArgumentParser() object
    ap.add_argument("-1","--image",required=True,help="input path to image file")
    args = vars(ap.parse_args())

    card = cv2.imread(args["image"])
    getCardFromImage(card)
