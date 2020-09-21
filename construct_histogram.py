import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
import argparse



def histogram3D(image, channels = 3, mask = None, bins = 16, size = 5000, moveOn = False):
    """
    Purpose: To relate the distribution of a three-dimensional image by matplotlib visualization.
    Parameters: an image (numpy array), number of channels (int)  defaulted to 3
    for 3D analysis, mask image (numpy array) defaulted to None, number of bins
    (int) for equal-width histogrammation defaulted to 8 for memory purposes,
    the size of the largest color bin (int) defaulted to 5000, a binary variable
    representing eventual user-supplied go-ahead (boolean) defaulted to False.
    Return: None, matplotlib.pyplot displays the histogram.
    """

    histogram = cv2.calcHist([image], list(range(0,channels)), mask, [bins,bins,bins], [0,256,0,256,0,256])

    fig = plt.figure() # instantiating matplotlib.pyplot.figure object
    ax = fig.add_subplot(111, projection = "3d")
    proportion = size / np.max(histogram) # ratio of input size to largest color bin in our image's histogram

    for (x, plane) in enumerate(histogram): # transvering indices representing decomposed blue bins
        for (y, row) in enumerate(plane): # transversing indices representing decomposed green bins
            for (z, column) in enumerate(row): # transvering indices representing decomposed red bins

                if histogram[x][y][z] > 0.0: # checking if there are pixels within this RGB bin
                    clusterSize = proportion * histogram[x][y][z] # scaled with respect to input size
                    RGB = (z/(bins-1), y/(bins-1), x/(bins-1)) # reversed as cv2.imread() stores bgr images
                    ax.scatter(x, y, z, s = clusterSize, facecolors = RGB)


    plt.show()
    if not moveOn:
        cv2.waitKey(0) # move on with any key input






if __name__ == '__main__':
    ap = argparse.ArgumentParser() # constructing ArgumentParser object
    ap.add_argument("-1","--image",required=True,help="input file path")
    ap.add_argument("-s","--size",required=False,help="size of largest color bin",default=5000)
    ap.add_argument("-b","--bins",required=False,help="number of bins per channel",default=8)
    args = vars(ap.parse_args())

    histogram3D(cv2.imread(args["image"]), args["bins"], args["size"])
