import cv2
import os
import numpy as np
from utils.utils import ReadPose


def judgeVio(video_path, json_dir, out_path, threshold):
    '''
    openpose POSE-25 keypoints ordering
    判断视频中的人是否摔倒，(1)先判断人体重心是否低于threshold; (2)判断人体重心下降的速度speed是否低于某个值; (3)重心在低水平内维持的时间超过某个值
    :param video_path:
    :param json_dir:
    :param out_path:
    :param threshold:
    :return:
    '''
    confidence = 0.0
    color = (255, 0, 0)
    n = 0
    count = 0      #记录低于一定阈值的帧数


    frames=cv2.VideoCapture(video_path)
    json_list=os.listdir(json_dir)
    counts=len(json_list)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')    #.mp4
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')    #.avi
    size = (int(frames.get(cv2.CAP_PROP_FRAME_WIDTH)), int(frames.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out = cv2.VideoWriter(out_path, fourcc, 20.0, size)

    if frames.isOpened() == False:
        print('Error opening video stream or file!')
    while (True):
        ret, frame = frames.read()
        if ret is False:
            break
        json_path = '{}/{}'.format(json_dir, json_list[n])
        n += 1
        # print(json_path)
        kps=ReadPose(json_path, confidence)

        for j in range(len(kps)):   #一帧中可能存在多个人
            lenMidHip = len(np.array([kps[j][8][1], kps[j][9][1], kps[j][12][1]]).nonzero()[0])
            lenMidAnkle=len(np.array([kps[j][11][1], kps[j][14][1]]).nonzero()[0])

            if lenMidHip != 0.:
                MidHip = (kps[j][8] + kps[j][9] + kps[j][12]) / lenMidHip
            else:
                MidHip = ([0., 0.])
            if lenMidAnkle != 0.:
                MidAnkle=(kps[j][11]+kps[j][14])/lenMidAnkle
            else:
                MidAnkle=([0., 0.])


        if MidAnkle[1] - MidHip[1] <= threshold:
            if count>=20:
                cv2.putText(frame, "Tumble", (int(frame.shape[0]/5), int(frame.shape[1]/5)), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 4)
            else:
                count+=1
                cv2.putText(frame, "{}".format(n), (int(MidHip[0]), int(MidHip[1])), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)

        out.write(frame)

    if count>=10:
        print('somebody tumbled!')
    frames.release()
    out.release()
    cv2.destroyAllWindows()


if __name__=='__main__':
    video_path = 'Data_row/TumbleVio/3.mp4'
    json_dir = 'Json/TumbleVio/3'
    out_path = 'Result/TumbleVio/3.mp4'
    threshold = 20

    judgeVio(video_path, json_dir, out_path, threshold)