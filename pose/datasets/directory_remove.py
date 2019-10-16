import cv2
import numpy as np
import os

images_file_path='/home/yxq/datasets/migu/motion_images8'
bg_file_path='/home/yxq/datasets/migu/motion_background8'

images_name=os.listdir(images_file_path)
bg_name=os.listdir(bg_file_path)

for i in range(len(bg_name)):
    b_name=bg_name[i].split('_')[0]
    for j in range(len(images_name)):
        img_name=images_name[j]
        if img_name==b_name:
            print('remove dictory: ', img_name)
            cmd='rm -r {}/{}'.format(images_file_path, img_name)
            os.system(cmd)
            continue
