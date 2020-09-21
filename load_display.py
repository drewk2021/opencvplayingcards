import cv2
import argparse

# testing out jpg input
ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required=False,help="input path to image file")
args = vars(ap.parse_args())

def getCardFromUser():
    """
    Purpose: To get an image of the desired card from the user.
    Parameters: None.
    Return: The image path (str) corresponding to a user-selected card.
    """

    valueSelected = False # user hasn't selected a value of the card
    values = list(range(2,11)) + ["J","Q","K","A"] # list of all card values
    cardValue = ""

    suitSelected = False # user hasn't selected a suit
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"] # list of 4 suits
    cardSuit = ""

    while not suitSelected:
        for (inDex, suit) in enumerate(suits):
            print(f"{suit}: ({inDex+1})")
        suitChosen = input("\nChoose your suit by the corresponding righthand index integers: ")

        if suitChosen in [str(i) for i in range(1,5)]: # stringified list of possible answer indices
            suitSelected = True
            cardSuit = suits[int(suitChosen)-1]
        else:
            print("Invalid input. Please choose from 1 to 4, depending on your preferred suit.\n")

    while not valueSelected:
        for (inDex, value) in enumerate(values):
            print(f"{value}: ({inDex+1})")
        valueChosen = input("\nChoose your value by the corresponding righthand index integers: ")

        if valueChosen in [str(i) for i in range(1,14)]: # stringified list of possible answer indices
            valueSelected = True
            cardValue = values[int(valueChosen)-1]
        else:
            print("Invalid input. Please choose from 1 to 13, corresponding to your preferred value.\n")


    print(f"\n You've selected the {cardValue} of {cardSuit}!\n")
    cardImagePath = f"img/cards-[{cardSuit[0]}{cardValue}]-001.jpg" # image Path, the '-001' corresponds to the hardwood background
    return cardImagePath


def display(image, description = None, moveOn = False):
    """
    Purpose: To display a given image within python's cv2 framework and wait
    (or not) for user's go-ahead.
    Parameters: An image (numpy array), an unrequired description describing
    said image (str), and an unnecessary binary variable defaulted at False
    corresponding to using (or not) the cv2.waitKey() function (boolean)
    Return: None.
    """
    cv2.imshow(description, image)
    if not moveOn:
        cv2.waitKey(0) # move on with any key input

# loading image with cv2
if __name__ == '__main__':
    display(cv2.imread(getCardFromUser()))
