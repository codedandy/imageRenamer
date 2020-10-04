import os.path
import urllib.parse

import reggie

def tryAgain():
    choice = input("Specified path not found, Re-enter path? [Y/n]: ")

    if choice.lower() == "y":
        pass
    elif choice.lower() == "n":
        print("Okay, shutting down.")
        quit()
    else:
        print("Input unrecognized.")
        pass


def verifyFilePath(path):
    pathCheck = os.path.isfile(path)

    if pathCheck:
        return 1
    else:
        return 0


def verifyImagePath(path):
    pathCheck = os.path.isdir(path)

    if pathCheck:
        return 1
    else:
        return 0


def compileImageFileList(path):
    initialList = os.listdir(path)

    filteredList = [urllib.parse.quote(image) for image in initialList if image.endswith((".jpg", ".gif", ".png"))]

    return filteredList


def continueProcess():
    while True:
        choice = input("Continue with processing? [Y/n]: ")

        if choice.lower() == "y":
            break
        elif choice.lower() == "n":
            print("Aborting process.")
            quit()
        else:
            print("Input not understood.")


def checkFileList(foundFileList, uniqueReferences):
    fileDiff = set(foundFileList) - set(uniqueReferences)
    refDiff = set(uniqueReferences) - set(foundFileList)

    fileMessage = f'{len(fileDiff)} file(s) found in folder that were not referred to in document:'
    refMessage = f'\n{len(refDiff)} reference(s) in document without corresponding files:'

    if len(fileDiff) > 0 and len(refDiff) > 0:
        print("Issues found with images and file references.")
        print(fileMessage)

        for file in fileDiff:
            print(urllib.parse.unquote(file))
        
        print(refMessage)

        for reference in refDiff:
            print(reference)
        
        continueProcess()

    elif len(fileDiff) > 0:
        print(fileMessage)

        for file in fileDiff:
            print(urllib.parse.unquote(file))
        
        continueProcess()

    elif len(refDiff) > 0:
        print(refMessage)

        for reference in refDiff:
            print(reference)
        
        continueProcess()

    else:
        print("• Sources match.")

def setImgPrefix():
    prefix = ""
    badChars = {"<", ">", ":", "\"", "/", "'", "\\", "|", "?", "*", " "}

    while True:
        prefix = input('Please enter an OS safe prefix for image names: ')

        charIntersection = badChars.intersection(prefix)

        # if len(set(prefix) - badChars) == len(set(prefix)):
        if len(charIntersection) == 0:
            break
        else:
            print(f"Risky character(s) {charIntersection} detected in string.")
    
    return prefix
