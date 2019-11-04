import xml.etree.ElementTree as ET
import os

FindPath="D:\Projects\YOLO\Annotations"
FileNames=os.listdir(FindPath)
xml_path="D:\Projects\YOLO\Annotations_new"

for file_name in FileNames:
    #print(file_name)
    if not os.path.isdir(file_name):
        in_file='{}\{}'.format(FindPath, file_name)
        out_file='{}\{}'.format(xml_path,file_name)
        #print(out_file)
        tree=ET.parse(in_file)
        root=tree.getroot()
        for name in root.iter('name'):
            print(name.text)
            if name.text=='婴儿车':
                name.text = str('Baby carriage')
        tree.write(out_file)



