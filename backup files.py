import time
import shutil
import os

def main() : 

    path = 'C:\Users\veba\Desktop'
    days = 30
    seconds = time.time()-(days*24*60*60)
    foldersCount = 0
    filesCount = 0

    if os.path.exists(path):
        for rootfolder,folders,files in os.walk(path):
            if seconds >= os.stat(path).st_ctime :
                remove(rootfolder)
                foldersCount += 1
                break
            else :
                for folder in folders:
                    folderPath = os.path.join(rootfolder,folder)
                    if seconds >= os.stat(folderPath).st_ctime :
                        remove(folderPath)
                        foldersCount += 1
                for file in files :
                    filePath = os.path.join(rootfolder,file)
                    if seconds >= os.stat(filePath).st_ctime :
                        removeFile(filePath)
                        filesCount += 1
        else :
            if seconds >= os.stat(filePath).st_ctime :
                removeFile(path)
                filesCount += 1
    else :
        print("Path doesn't exist!")
    print(f"total deleted folders : {foldersCount}")
    print(f"total deleted files : {filesCount}")

def remove(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed sucessfully")
    else:
        print(f"unable to delete {path}")

def removeFile(path):
    if not os.remove(path):
        print(f"{path} is removed sucessfully")
    else:
        print(f"unable to delete {path}")


if __name__ == '__main__':
    main()