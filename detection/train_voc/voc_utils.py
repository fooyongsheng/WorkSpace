import xml.etree.ElementTree as ET
import os
import random
import shutil


def rename_png(root_img, aim_img):
    if not os.path.exists(aim_img):
        os.mkdir(aim_img)
    for name in os.listdir(root_img):
        root_name = root_img + name
        # modify image extension
        aim_name = aim_img + name.split('.')[0] + '.png'
        shutil.copyfile(root_name, aim_name)


def move_image(root_img, aim_img):
    for name in os.listdir(root_img):
        if not os.path.exists(aim_img):
            os.mkdir(aim_img)
        shutil.copyfile(root_img + name, aim_img + name.split('.')[0] + '.png')


def move_image_accord_xml(root_img, root_xml, aim_img):
    if not os.path.exists(aim_img):
        os.mkdir(aim_img)
    xml_list = os.listdir(root_xml)
    for name in os.listdir(root_img):
        if name.split('.')[0] + '.xml' not in xml_list:
            continue
        shutil.copyfile(root_img + name, aim_img + name)

def generate_data_list(root):
    dest_root = root
    imgs_path = os.path.join(dest_root, 'JPEGImages')
    path1 = os.path.join(dest_root, 'ImageSets')
    path2 = os.path.join(path1, 'Main')
    if not os.path.exists(path1):
        os.mkdir(path1)
        os.mkdir(path2)
    out_path_train = '{}/train.txt'.format(path2)
    out_path_test = '{}/test.txt'.format(path2)

    imgs = os.listdir(imgs_path)
    # imgs.sort(key=lambda x: (int(x.split('_')[0][1:]), float(x.split('_')[1]), float(x.split('_')[2])))
    length = len(imgs)
    t = 0.6
    thr = int(length*t)
    random.shuffle(imgs)
    imgs_train = imgs[:thr]
    imgs_test = imgs[thr:]
    with open(out_path_train, 'w') as f_train:
        for count, data_single in enumerate(imgs_train):
            f_train.write('{}\n'.format(os.path.splitext(data_single)[0]))
            print('\r{}/{}'.format(count+1, len(imgs_train)), end='')
    print()
    with open(out_path_test, 'w') as f_test:
        for count, data_single in enumerate(imgs_test):
            f_test.write('{}\n'.format(os.path.splitext(data_single)[0]))
            print('\r{}/{}'.format(count + 1, len(imgs_test)), end='')
    print()


class VocLabel:
    # x, y, w, h
    def __init__(self, root):
        self.root = root
        self.sets = [('HW_car', 'train'), ('HW_car', 'test')]
        self.classes = ['car']
        # self.sets = [('_test', 'train'), ('_test', 'test')]
        # self.classes = ['red', 'blue', 'yellow']

    def convert(self, size, box):
        dw = 1./size[0]
        dh = 1./size[1]
        x = (box[0] + box[1])/2.0
        y = (box[2] + box[3])/2.0
        w = box[1] - box[0]
        h = box[3] - box[2]
        x = x*dw
        w = w*dw
        y = y*dh
        h = h*dh
        return x, y, w, h

    def convert_annotation(self, year, image_id):
        in_file = open('{}/Annotations/{}.xml'.format(self.root, image_id))
        out_file = open('{}/labels/{}.txt'.format(self.root, image_id), 'w')
        tree = ET.parse(in_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)

        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in self.classes or int(difficult) == 1:
                continue
            cls_id = self.classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = self.convert((w, h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

    def forward(self):
        for year, image_set in self.sets:
            if not os.path.exists('{}/labels/'.format(self.root)):
                os.makedirs('{}/labels/'.format(self.root))
            image_ids = open('{}/ImageSets/Main/{}.txt'.format(self.root, image_set)).read().strip().split('\n')
            list_file = open('{}/{}_{}.txt'.format(self.root, year, image_set), 'w')
            for count, image_id in enumerate(image_ids):
                list_file.write('{}/JPEGImages/{}.png\n'.format(self.root, image_id))
                self.convert_annotation(year, image_id)
                print('\r{}/{}'.format(count + 1, len(image_ids)), end='')
            print()
            list_file.close()

if __name__ == '__main__':
    generate_data_list(r'/home/yxq/Projects/darknet/train_my_data/HW_car/VOC2007')
    voclabel = VocLabel(r'/home/yxq/Projects/darknet/train_my_data/HW_car/VOC2007')
    voclabel.forward()
    #move_image_accord_xml(root_img, root_xml, aim_img)
    print('process finish')
