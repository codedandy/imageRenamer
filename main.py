import os
import os.path
import shutil
import time

import verifier
import fileWork
import reggie

print("-= Quae Imago Est =-")
print("This program works with absolute paths.")
print("Intended file types for use: .html, .xhtml, .jpg, .png, .gif.")

# obtain paths and verify paths exist
sourceFile = ""
sourceFolder = ""

while True:
    sourceFile = input("Enter source HTML file path: ")
    control = verifier.verifyFilePath(sourceFile)

    if control == 1:
        break
    else:
        verifier.tryAgain()

while True:
    sourceFolder = input("Enter source image folder file path: ")
    control = verifier.verifyImagePath(sourceFolder)

    if control == 1:
        break
    else:
        verifier.tryAgain()

# open source doc
print("• Reading source file.")
time.sleep(1)
workingFile = fileWork.openReadFile(sourceFile)

# scan source file for images
print("• Identifying image references.")
time.sleep(1)
fileImageRefs = reggie.imgRegex.findall(workingFile)

print("• Filtering image paths.")
time.sleep(1)
filteredImages = reggie.removeFilePath(fileImageRefs)

uniqueReferences = list(set(filteredImages))
print(f'• Number of unique image references: {len(uniqueReferences)}')

# print(f'Debug object(s): {filteredImages[0:2]}')
# print(f'Debug object(s): {len(uniqueReferences)}')



