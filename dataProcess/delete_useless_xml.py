import os
import shutil


imagePath="F:\\Unattended_Cabinet\\JPEGImages\\林哒儿系列"
xmlPath="F:\\Unattended_Cabinet\\Annotations\\Lindaer"

outPath="F:\\Unattended_Cabinet\\Annotations2\\Lindaer"
if not os.path.exists(outPath):
    os.mkdir(outPath)


imgList=os.listdir(imagePath)
xmlList=os.listdir(xmlPath)


for img in imgList:
    print('image:', img)
    image=img.split('.')[0]+img.split('.')[1]+img.split('.')[2]

    if len(xmlList)>0:
        for xml in xmlList:
            print('xml:',xml)
            xmlFile=xml.split('.')[0]+xml.split('.')[1]+xml.split('.')[2]

            if xmlFile==image:
                inxml=os.path.join(xmlPath, xml)
                outxml=os.path.join(outPath, xml)

                shutil.copy(inxml, outxml)
                xmlList.remove(xml)
                print('copy:', xml)

                #os.remove(inxml)
                break
    print('lenxmlFiles:', len(xmlList))










