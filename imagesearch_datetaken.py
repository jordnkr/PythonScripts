import os
from PIL import Image
from pathlib import Path

def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

def main():
    while True:
        fp = input("Folder path:")
        #dt = input("Date Taken:")
        for root, dirs, files in os.walk(fp):
            path = root.split(os.sep)
            #print((len(path) - 1) * '---', os.path.basename(root))
            for file in files:
                #print(len(path) * '---', os.path.join(root, file))
                fullFile = os.path.join(root, file)
                if (fullFile.endswith('.jpg')):
                    print(fullFile) 
        again = input("Look again? (y/n):")
        if (again != "y"):
            break
main()