## check this for syntax: https://www.geeksforgeeks.org/modify-xml-files-with-python/
# dataset from: https://data.mendeley.com/datasets/rnhz3fvbj2
### to fit the file into google colab ###

import shutil
import glob
import os
from collections import namedtuple
import xml.etree.ElementTree as ET
import sys



### to split training and validation ###
directory = r"/home/samer/Desktop/SurgicalWasteDataset/Surgicalwastedataset/"
dir = "/home/samer/Desktop/SurgicalWasteDataset/Surgicalwastedataset/train/"
dic = "/home/samer/Desktop/SurgicalWasteDataset/Surgicalwastedataset/validation/"
image_list = []
anno_list = []
counter = 200

for fily in os.listdir(directory):
    if counter < 200:
        break
    else:
        counter += 1
        x = glob.glob(rf'/home/samer/Desktop/SurgicalWasteDataset/Surgicalwastedataset/{counter}.jpg')[0]
        shutil.move(x, dir)
        y = glob.glob(rf'/home/samer/Desktop/SurgicalWasteDataset/Surgicalwastedataset/{counter}.xml')[0]
        shutil.move(y, dir)
        continue

### to split annotations from images ###
dest_dir = "/home/samer/Desktop/SurgicalWasteDataset/Surgicalwastedataset/validation/images/"
counter = 0
for file in glob.glob(r'/home/samer/Desktop/SurgicalWasteDataset/Surgicalwastedataset/validation/*.jpg'):
    print("beedoo")
    shutil.move(file,dest_dir)

### to rename the annotations and images ### 
directorya = os.chdir("/home/samer/Desktop/SurgicalWasteDataset/Surgicalwastedataset/annotations/")
dic = os.chdir("/home/samer/Desktop/SurgicalWasteDataset/Surgicalwastedataset/images/")
names1 = []
counter = 0

for file_name in os.listdir(directorya):
    name1,ext1 = os.path.splitext(file_name)
    names1.append(name1)
for f_name in os.listdir(dic):
    name2,ext2 = os.path.splitext(f_name)
    counter += 1
    if name2 == names1[counter-1]:
        print(counter)
        os.rename("/home/samer/Desktop/SurgicalWasteDataset/Surgicalwastedataset/images/"+name2+ext2, "/home/samer/Desktop/SurgicalWasteDataset/Surgicalwastedataset/images/"+str(counter)+ext2)
        os.rename("/home/samer/Desktop/SurgicalWasteDataset/Surgicalwastedataset/annotations/"+name2+".xml", "/home/samer/Desktop/SurgicalWasteDataset/Surgicalwastedataset/annotations/"+str(counter)+".xml")


### to edit the xml files ###
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






