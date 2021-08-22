from zipfile import ZipFile
import docx2txt
import os

def main():
    while True:
        fp = input("Folder path:")
        st = input("Search term:")
        try:
            files = []
            for zip_name in os.listdir(fp):
                with ZipFile(os.path.join(fp, zip_name)) as zip_file:
                    for file in zip_file.namelist():
                        with zip_file.open(file) as doc:
                            content = docx2txt.process(doc)
                            if st in content:
                                files.append(zip_name + '/' + file)
            print("\n".join(files))
            break
        except FileNotFoundError:
            print("File path not found.")

main()