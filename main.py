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

uniqueReferences = set(filteredImages)
print(f'• Number of unique image references: {len(uniqueReferences)}')

# check file folder for images
print("• Checking for files in specified directory.")
foundFileList = verifier.compileImageFileList(sourceFolder)

print(f'• {len(foundFileList)} image file(s) in directory, {len(uniqueReferences)} unique image reference(s) found in document.')
time.sleep(1)

# execute diff checks of file list to see if it is referenced and vice versa
print("• Comparing document references versus file list.")
verifier.checkFileList(foundFileList, uniqueReferences)
time.sleep(1)

# create backups of source file and contents of the image folder
print("• Creating backups.")
fileWork.createBackups(sourceFile, sourceFolder)
time.sleep(1)

# input desired image prefix
prefixString = verifier.setImgPrefix()
time.sleep(1)

# build list of tuples with the original reference name (uniqueReferences) 
# and the new sequential name, 
# if the reference is in the otherListComp then skip that ref

renamedImageSets = fileWork.assembleNewNames(prefixString, filteredImages)
time.sleep(1)

print("• Renaming images in source document.")
updatedFile = fileWork.updateSourceFile(workingFile, renamedImageSets)
time.sleep(1)

print("• Saving changes to source document.")
fileWork.saveSourceDocument(sourceFile, updatedFile)
time.sleep(1)

print("• Renaming image files.")
fileWork.renameImageFiles(sourceFolder, renamedImageSets)
time.sleep(1)

print("-= Quae Quod Phantasticum =-")
