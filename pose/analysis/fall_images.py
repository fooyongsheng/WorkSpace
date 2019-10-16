import cv2
import os
import numpy as np
from utils.utils import ReadPose


def tumbleImgs(image_dir, json_dir, out_dir, threshold):
    '''
    parse the openpose COCO-18 keypoints ordering
    :param image_dir:
    :param json_dir:
    :param out_dir:
    :param threshold:
    :return:
    '''
    confidence = 0.0
    color = (0,0,255)
    point_color=(255,0,0)

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    image_list=os.listdir(image_dir)
    json_list=os.listdir(json_dir)

    image_list_sort = []
    for img in image_list:
        img_num = img.split('.')[0]
        image_list_sort.append(int(img_num))
        image_list_sort.sort()

    json_list_sort = []
    for js in json_list:
        js_num = js.split('.')[0]
        json_list_sort.append(int(js_num))
        json_list_sort.sort()

    for img, js in zip(image_list_sort, json_list_sort):
        img='{}.jpg'.format(img)
        js='{}.json'.format(js)
        json_path='{}\{}'.format(json_dir, js)
        image_path='{}\{}'.format(image_dir, img)

        kps=ReadPose(json_path, confidence)
        image = cv2.imread(image_path)

        for j in range(len(kps)):
            Rhip=kps[j][8]
            Lhip=kps[j][11]
            Rank=kps[j][10]
            Lank=kps[j][13]
            Neck=kps[j][1]

            MidHip=(Rhip+Lhip)/2
            MidAnkle=(Rank+Lank)/2

            if MidAnkle[1]-MidHip[1]<=threshold or MidHip[1]-Neck[1]<=threshold:
                cv2.circle(image, (int(MidHip[0]), int(MidHip[1])), 2, point_color, 2)
                cv2.circle(image, (int(MidAnkle[0]), int(MidAnkle[1])), 2, point_color, 2)
                cv2.circle(image, (int(Neck[0]), int(Neck[1])), 2, point_color, 2)
                cv2.putText(image, "T" , (int(MidHip[0]), int(MidHip[1])), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)
        out_path = '{}\{}'.format(out_dir, img)
        cv2.imwrite(out_path, image)
    print('Finished! You can check the output images on {}'.format(out_dir))


def tumbleImg(image_path, json_path, threshold):
    '''
    parse the openpose COCO-18 keypoints ordering
    :param image_path:
    :param json_path:
    :param threshold:
    :return:
    '''
    confidence = 0.0
    color = (0,0,255)
    point_color=(255,0,0)

    image = cv2.imread(image_path)
    kps = ReadPose(json_path, confidence)

    for j in range(len(kps)):
        Rhip=kps[j][8]
        Lhip=kps[j][11]
        Rank=kps[j][10]
        Lank=kps[j][13]
        Neck=kps[j][1]


        MidHip=(Rhip+Lhip)/len(np.array([Rhip[1],Lhip[1]]).nonzero()[0])
        MidAnkle=(Rank+Lank)/len(np.array([Rank[1],Lank[1]]).nonzero()[0])

        print(Neck[1])
        print(MidHip[1])
        print(MidAnkle[1])

        if MidAnkle[1]-MidHip[1]<=threshold or MidHip[1]-Neck[1]<=threshold:
            cv2.circle(image, (int(MidHip[0]), int(MidHip[1])), 2, point_color, 2)
            cv2.circle(image, (int(MidAnkle[0]), int(MidAnkle[1])), 2, point_color, 2)
            cv2.circle(image, (int(Neck[0]), int(Neck[1])), 2, point_color, 2)
            cv2.putText(image, "T" , (int(MidHip[0]), int(MidHip[1])), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

    cv2.imshow('image',image)
    cv2.waitKey(0)


def judgeImg(image_path, json_path, threshold):
    '''
    parse the openpose POSE-25 keypoints ordering
    :param image_path:
    :param json_path:
    :param threshold:
    :return:
    '''
    confidence = 0.0
    color = (0, 0, 255)
    point_color = (255, 0, 0)

    image = cv2.imread(image_path)
    kps = ReadPose(json_path, confidence)

    for j in range(len(kps)):
        Neck=kps[j][1]
        lenMidHip=len(np.array([kps[j][8][1],kps[j][9][1],kps[j][12][1]]).nonzero()[0])
        lenMidAnkle=len(np.array([kps[j][11][1],kps[j][14][1]]).nonzero()[0])
        if lenMidHip != 0.:
            MidHip=(kps[j][8]+kps[j][9]+kps[j][12])/lenMidHip
        else:
            MidHip=([0.,0.])
        if lenMidAnkle != 0.:
            MidAnkle = (kps[j][11] + kps[j][14]) / lenMidAnkle
        else:
            MidAnkle=([0.,0.])

        print(Neck[1])
        print(MidHip[1])

        if MidAnkle[1]-MidHip[1]<=threshold or MidHip[1]-Neck[1]<=threshold:
            cv2.circle(image, (int(MidHip[0]), int(MidHip[1])), 2, point_color, 2)
            cv2.circle(image, (int(MidAnkle[0]), int(MidAnkle[1])), 2, point_color, 2)
            cv2.circle(image, (int(Neck[0]), int(Neck[1])), 2, point_color, 2)
            cv2.putText(image, "T" , (int(MidHip[0]), int(MidHip[1])), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

    cv2.imshow('image',image)
    cv2.waitKey(0)


def judgeImgs(image_dir, json_dir, out_dir, threshold):
    '''
    parse the openpose POSE-25 keypoints ordering
    :param image_dir:
    :param json_dir:
    :param out_dir:
    :param threshold:
    :return:
    '''
    confidence = 0.0
    color = (0,0,255)
    point_color=(255,0,0)

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    image_list=os.listdir(image_dir)
    json_list=os.listdir(json_dir)

    image_list_sort = []
    for img in image_list:
        img_num = img.split('.')[0]
        image_list_sort.append(int(img_num))
        image_list_sort.sort()

    json_list_sort = []
    for js in json_list:
        js_num = js.split('_')[0]
        json_list_sort.append(int(js_num))
        json_list_sort.sort()

    for img, js in zip(image_list_sort, json_list_sort):
        img='{}.jpg'.format(img)
        js='{}_keypoints.json'.format(js)
        json_path='{}\{}'.format(json_dir, js)
        image_path='{}\{}'.format(image_dir, img)

        kps=ReadPose(json_path, confidence)
        image = cv2.imread(image_path)

        for j in range(len(kps)):
            Neck = kps[j][1]
            lenMidHip = len(np.array([kps[j][8][1], kps[j][9][1], kps[j][12][1]]).nonzero()[0])
            lenMidAnkle = len(np.array([kps[j][11][1], kps[j][14][1]]).nonzero()[0])
            if lenMidHip != 0.:
                MidHip = (kps[j][8] + kps[j][9] + kps[j][12]) / lenMidHip
            else:
                MidHip = ([0., 0.])
            if lenMidAnkle != 0.:
                MidAnkle = (kps[j][11] + kps[j][14]) / lenMidAnkle
            else:
                MidAnkle = ([0., 0.])


            if MidAnkle[1]-MidHip[1]<=threshold or MidHip[1]-Neck[1]<=threshold:
                cv2.circle(image, (int(MidHip[0]), int(MidHip[1])), 2, point_color, 2)
                cv2.circle(image, (int(MidAnkle[0]), int(MidAnkle[1])), 2, point_color, 2)
                cv2.circle(image, (int(Neck[0]), int(Neck[1])), 2, point_color, 2)
                cv2.putText(image, "T" , (int(MidHip[0]), int(MidHip[1])), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)
        out_path = '{}\{}'.format(out_dir, img)
        cv2.imwrite(out_path, image)
    print('Finished! You can check the output images on {}'.format(out_dir))




if __name__=='__main__':
    image_dir = 'Data_row\TumbleImg'
    json_dir = 'Json\TumbleImg_json'
    out_dir = 'Result\TumbleImg'

    image_path = 'Data_row/TumbleImg/4.jpg'
    json_path = 'Json/TumbleImg_json/4_keypoints.json'
    out_path = 'Result/output.png'
    threshold=30

    # tumbleImgs(image_dir, json_dir, out_dir, threshold)
    tumbleImg(image_path, json_path, threshold)
    #judgeImg(image_path, json_path, threshold)

    #judgeImgs(image_dir, json_dir, out_dir, threshold)

