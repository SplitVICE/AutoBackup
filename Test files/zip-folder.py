import os
import zipfile

zf = zipfile.ZipFile("myzipfile.zip", "w")
for dirname, subdirs, files in os.walk("folderContent"):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()

#Source: https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory-in-python