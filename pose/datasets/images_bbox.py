# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

import sys, os

sys.path.append(os.path.join(os.getcwd(), 'python/'))
import cv2
import numpy as np
from timeit import default_timer as timer

import darknet as dn

dn.set_gpu(0)
net = dn.load_net(b"cfg/yolov3.cfg", b"weights/yolov3.weights", 0)
meta = dn.load_meta(b"cfg/coco.data")


def bbox_image(image_path):
    res = dn.detect(net, meta, image_path, thresh=.5, hier_thresh=.5, nms=.45)

    if len(res) > 0:
        for i in range(len(res)):
            if res[i][0]==b'person':
                bbox = res[i][2]

                center_x = bbox[0]
                center_y = bbox[1]
                width = bbox[2]
                height = bbox[3]
    
                left_top_x=center_x-width/2
                left_top_y=center_y-height/2
                bbox = np.array([left_top_x, left_top_y, width, height])
            else:
                bbox=np.array([0., 0., 0., 0.])
    else:
        bbox = np.array([0., 0., 0., 0.])
    return bbox


def bbox_images():
    images_in_path = '/home/yxq/datasets/migu/motion_list_images'
    images_dic_list = os.listdir(images_in_path)

    bboxes_out_path = '/home/yxq/datasets/migu/motion_list_bbox'
    if not os.path.exists(bboxes_out_path):
        os.mkdir(bboxes_out_path)

    for i in range(len(images_dic_list)):
        images_path = '{}/{}'.format(images_in_path, images_dic_list[i])
        name_list = os.listdir(images_path)

        output_path = '{}/{}'.format(bboxes_out_path, images_dic_list[i].split('.')[0])
        if not os.path.exists(output_path):
            os.mkdir(output_path)

        for k in range(len(name_list)):
            image_path = '{}/{}'.format(images_path, name_list[k])
            temp=cv2.imread(image_path)
            cv2.imwrite('/home/yxq/datasets/migu/temp.png', temp)
            bbox = bbox_image(b'/home/yxq/datasets/migu/temp.png')


            # cv2.rectangle(temp, (int(bbox[0]), int(bbox[1])),
			# 	(int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3])), (0,0,255),2)
            # cv2.imshow('result', temp)
            # cv2.waitKey(1000)

            bbox_out_path = "{}/{}.txt".format(output_path, name_list[k].split('.')[0])
            np.savetxt(bbox_out_path, bbox, fmt='%0.2f')
        print('finish one images file'.format(images_dic_list[i].split('.')[0]))

if __name__ == '__main__':
    # image_path=b'/home/yxq/datasets/migu/motion_list_images/A001b/0.png'
    # bbox=bbox_image(image_path)
    # print(bbox)

    bbox_images()






