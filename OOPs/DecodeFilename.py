import os
import re

def main():
    def decoder(_path):
        print(os.path.abspath(_path))
        files = [i for i in os.listdir(os.path.abspath(_path))]
        print(files)
        os.chdir(_path)
        for file in files :
            os.rename(file, re.sub(r"\d+\W","", file))

    print("Please enter the directory name of the files: (relative path):")
    path = input()
    try:
        decoder(path)
        print("files successfully decoded")
    except Exception as e:
        print(str(e))


if __name__ =="__main__":
    main()



