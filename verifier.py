import os.path

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


