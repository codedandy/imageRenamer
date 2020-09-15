import os
import os.path
import shutil

def openReadFile(filePath):
    try:
        openFile = open(filePath)
        readFile = openFile.read()
        openFile.close()

        return readFile
    except Exception:
        print("Problem reading file, aborting.")
        quit()