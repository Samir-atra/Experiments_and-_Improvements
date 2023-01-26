## check this for syntax: https://www.geeksforgeeks.org/modify-xml-files-with-python/
# dataset from: https://data.mendeley.com/datasets/rnhz3fvbj2
### to fit the file into google colab ###

import shutil
import glob
import os
import xml.etree.ElementTree as ET
import sys


class setup():

    def __init__(self, datapath):             
        self.datapath = datapath

    @property
    def renamer(self):
        ### to rename the annotations and images ### 
        directory = os.chdir(f"{self.datapath}")
        # dic = os.chdir(f"{self.datapath}images/")
        inames = []
        anames = []
        counter = 0
        for file_name in os.listdir(directory):
            name,ext = os.path.splitext(file_name)
            if ext == ".jpg":
                inames.append(name)
                continue
            elif ext == ".xml":
                anames.append(name)
                continue
        for image_name in inames:
            counter += 1
            for excel_name in anames:
                if  image_name == excel_name:
                    print(counter)
                    os.rename(f"{self.datapath}"+image_name+".jpg", f"{self.datapath}"+str(counter)+".jpg")
                    os.rename(f"{self.datapath}"+image_name+".xml", f"{self.datapath}"+str(counter)+".xml")

    @property
    def first_splitter(self):
        ### to split training and validation ###
        directory = rf"{self.datapath}"
        dir = f"{directory}train/"
        dic = f"{directory}validation/"
        counter = 0
        for fily in os.listdir(directory):
            if counter <= 998:
                counter += 1
                print(counter)
                x = glob.glob(rf'{self.datapath}{counter}.jpg')[0]
                shutil.move(x, dir)
                y = glob.glob(rf'{self.datapath}{counter}.xml')[0]
                shutil.move(y, dir)
                continue
            else:
                counter += 1
                print(counter)
                x = glob.glob(rf'{self.datapath}{counter}.jpg')[0]
                shutil.move(x, dic)
                y = glob.glob(rf'{self.datapath}{counter}.xml')[0]
                shutil.move(y, dic)
                continue

    @property
    def second_splitter(self):
        ### to split annotations from images ###
        destinations = ["train/images/", "train/annotations/", "validation/images/", "validation/annotations/"]
        files = ["train/*.jpg", "train/*.xml", "validation/*.jpg", "validation/*.xml"]
        counter = 0
        for num in range(len(destinations)):
            dest_dir = f"{self.datapath}{destinations[num]}"
            counter += 1
            for file in glob.glob(rf'{self.datapath}{files[num]}'):
                print(counter)
                shutil.move(file,dest_dir)


    def editor(self):
        ### to edit the xml files ### just a draft #####
        dir = sys.argv[1]
        counter = 200
        for file in os.listdir(dir):
            name2,ext2 = os.path.splitext(file)
            counter += 1
            tree = ET.parse(dir+str(name2)+".xml")
            root = tree.getroot()

            child = root.findall("filename")[0]
            print(child.text)
            print(counter)
            child.text = (str(name2 + ".jpg"))
            tree.write(dir+file)
            print(child.text)


try:
    sety = setup(sys.argv[1])
except IndexError:
    sys.exit("InputError:example usage: python DatasetSetup.py /data/set/directory/path/")

fun = input("input function, one of (renamer, first_splitter, second_splitter): ")
getattr(sety, fun)
# sety.renamer()
# sety.first_splitter()
# sety.second_splitter()




