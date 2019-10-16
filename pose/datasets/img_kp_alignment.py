import cv2
import os
import json
import numpy as np


def sort_kpJson(lists):
    sorted_lists=[]
    ret_lists=[]
    for i in range(len(lists)):
        kp_name=lists[i].split('_')[1].lstrip('0')
        if kp_name != '':
            sorted_lists.append(int(kp_name))
        else:
            sorted_lists.append(0)
    sorted_lists.sort()

    for i in range(len(sorted_lists)):
        ret_lists.append('{}_{}_keypoints.json'.format(lists[i].split('_')[0], str(sorted_lists[i]).zfill(12)))
    return ret_lists


def rename_jsons():
    keypoints_dir = '/home/yxq/datasets/migu/motion_background1/motion_keypoints'
    keypoints_dir_names = os.listdir(keypoints_dir)
    keypoints_dir_names.sort(key=lambda x: x)

    n=0
    for i in range(len(keypoints_dir_names)):
        keypoints_in_path = '{}/{}'.format(keypoints_dir, keypoints_dir_names[i])
        keypoints_list = os.listdir(keypoints_in_path)
        keypoints_list = sort_kpJson(keypoints_list)

        for j in range(len(keypoints_list)):
            kp_src=os.path.join(os.path.abspath(keypoints_in_path), keypoints_list[j])
            kp_dst=os.path.join(os.path.abspath(keypoints_in_path), '{}.json'.format(str(n).zfill(12)))
            os.rename(kp_src, kp_dst)
            n+=1
        print('rename {} json finish!'.format(keypoints_dir_names[i]))


def rename_images():
    images_dir='/home/yxq/datasets/migu/motion_background1/motion_background'
    images_dir_names=os.listdir(images_dir)
    images_dir_names.sort(key=lambda x: x)  #按照文件排列顺序读取文件

    n = 0
    for i in range(len(images_dir_names)):
        images_in_path = '{}/{}'.format(images_dir, images_dir_names[i])
        images_list = os.listdir(images_in_path)
        images_list.sort(key=lambda x: int(x.split('.')[0]))

        for j in range(len(images_list)):
            kp_src = os.path.join(os.path.abspath(images_in_path), images_list[j])
            kp_dst = os.path.join(os.path.abspath(images_in_path), '{}.png'.format(str(n).zfill(12)))
            os.rename(kp_src, kp_dst)
            n += 1
        print('rename {} images finish!'.format(images_dir_names[i]))


def read_keypoints(json_path):
    json_file = open(json_path, encoding='utf-8')
    jsons = json_file.read()

    dicts = json.loads(jsons)
    people = dicts['people']

    multi_keypoints = []
    for p in range(len(people)):   # for multiple people
        kps = people[p]['pose_keypoints_2d']
        kps = np.array(kps).reshape(-1, 3)
        multi_keypoints.append(kps)
    return multi_keypoints



def test_alignment():
    image_path='/home/yxq/datasets/migu/motion_background1/images/260.png'
    json_path='/home/yxq/datasets/migu/motion_background1/keypoints/260.json'

    multi_keypoints=read_keypoints(json_path)
    image=cv2.imread(image_path)

    point = []
    points = []
    for i in range(len(multi_keypoints)):  # the number of people
        for j in range(len(multi_keypoints[i])):  # the number of key points
            point.append((int(multi_keypoints[i][j][0]), int(multi_keypoints[i][j][1])))
        points.append(point)

    for i in range(len(points)):  # the number of people
        k = 0  # flag the label of number
        for pt in points[i]:
            cv2.circle(image, pt, 2, (255, 0, 0), 2)
            cv2.putText(image, str(k), pt, cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
            k += 1

    cv2.imshow('img', image)
    cv2.waitKey(0)



if __name__ == '__main__':
    rename_images()
    # rename_jsons()
    test_alignment()





















