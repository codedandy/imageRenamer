import os
import os.path
import shutil
import urllib.parse

def openReadFile(filePath):
    try:
        openFile = open(filePath)
        readFile = openFile.read()
        openFile.close()

        return readFile
    except Exception:
        print("Problem reading file, aborting.")
        quit()


def createBackups(sourceFile, sourceFolder):
        os.chdir(sourceFolder)
        os.chdir("../")

        if os.path.isdir(f'{os.getcwd()}/backup'):
            shutil.rmtree(f'{os.getcwd()}/backup')
        else:
            pass
        
        try:
            os.makedirs("backup")
            shutil.copy(sourceFile, f'{os.getcwd()}/backup')
            shutil.copytree(sourceFolder, f'{os.getcwd()}/backup/images')
            print("• Backups created.")
        except Exception as e:
            print(f'!!! Exception raised:\n{e}\n-= Shutting Down Process =-')
            quit()


def assembleNewNames(prefixString, filteredImages):
    newNameList = []
    imageCounter = 0
    processedRefs = []

    for image in filteredImages:
        imageCounter += 1
        imageExt = ""

        if image in processedRefs:
            print(f'- Skipping duplicate reference: {image}')
        else:
            if ".jpg" in image:
                imageExt = ".jpg"
            elif ".png" in image:
                imageExt = ".png"
            elif ".gif" in image:
                imageExt = ".gif"
            else:
                pass
            
            if imageCounter < 10:
                newNameList.append((image, f'{prefixString}_00{imageCounter}{imageExt}'))
            elif imageCounter < 100:
                newNameList.append((image, f'{prefixString}_0{imageCounter}{imageExt}'))
            else:
                newNameList.append((image, f'{prefixString}_{imageCounter}{imageExt}'))
            
            processedRefs.append(image)
    
    return newNameList


def updateSourceFile(workingFile, renamedImageSets):
    for imageRef in renamedImageSets:
        try:
            print(f'-- Replacing {imageRef[0]} with {imageRef[1]}')
            workingFile = workingFile.replace(imageRef[0], imageRef[1])
        except Exception as e:
            print(f'!!! Exception replacing {imageRef[0]} with reason given:\n{e}')
    
    return workingFile

def saveSourceDocument(sourceFile, updatedFile):
    try:
        rewriteFile = open(sourceFile, "w")
        rewriteFile.write(updatedFile)
        rewriteFile.close()
    except Exception as e:
        print(f'!!! Exception raised while saving:\n{e}')

def renameImageFiles(sourceFolder, renamedImageSets):
    for imageRef in renamedImageSets:
        try:
            os.rename(f'{sourceFolder}/{imageRef[0]}', f'{sourceFolder}/{imageRef[1]}')
            print(f'-- Image file {imageRef[0]} being renamed {imageRef[1]}')
        except OSError:
            os.rename(urllib.parse.unquote(f'{sourceFolder}/{imageRef[0]}'), f'{sourceFolder}/{imageRef[1]}')
            print(f'-- Image file {urllib.parse.unquote(imageRef[0])} being renamed {imageRef[1]}')
        except Exception as e:
            print(f'!!! Exception raised for {imageRef[0]}: {e}')