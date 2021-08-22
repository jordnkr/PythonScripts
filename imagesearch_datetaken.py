import os
from PIL import Image

def get_date_taken(path):
    try:
        return Image.open(path)._getexif()[36867]
    except:
        return False

def main():
    while True:
        fp = input("Folder path:")
        dt = input("Date Taken (YYYY:MM:DD):")
        for root, dirs, files in os.walk(fp):
            for file in files:
                full_path = os.path.join(root, file)
                if (full_path.lower().endswith(('.jpg', '.jpeg'))):
                    date_taken = get_date_taken(full_path)
                    if date_taken:
                        if (dt == date_taken.split(" ")[0]):
                            print(full_path)
        again = input("Look again? (y/n):")
        if (again != "y"):
            break

main()