import cv2
import os
import numpy as np

from utils.utils import get_keypoints

def fall_video(video_path, json_dir, out_path, threshold):
    json_list=os.listdir(json_dir)
    json_list=[json_list[i].split('.')[0] for i in range(len(json_list))]
    json_list=[int(json_list[i]) for i in range(len(json_list))]
    json_list.sort()
    json_list=[str(json_list[i]) +'.json' for i in range(len(json_list))]

    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fourcc=cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    frames, size=get_frames(video_path)
    out=cv2.VideoWriter(out_path, fourcc, 10.0, size)

    k=0   #取视频序列
    n=0   #取json序列
    count=0   #记录低于阈值的帧数

    for i in range(len(frames)):
        json_name=json_list[n].split('.')[0]
        if int(json_name) != k:
            k += 1
        else:
            json_path='{}/{}'.format(json_dir, json_list[n])
            n += 1

            keypoints=get_keypoints(json_path)
            for j in range(len(keypoints)):
                lenMidHip = len(np.array([keypoints[j][8][1], keypoints[j][9][1], keypoints[j][12][1]]).nonzero()[0])
                lenMidAnkle = len(np.array([keypoints[j][11][1], keypoints[j][14][1]]).nonzero()[0])

                if lenMidHip != 0.:
                    MidHip = (keypoints[j][8] + keypoints[j][9] + keypoints[j][12]) / lenMidHip
                else:
                    MidHip = ([0., 0.])
                if lenMidAnkle != 0.:
                    MidAnkle = (keypoints[j][11] + keypoints[j][14]) / lenMidAnkle
                else:
                    MidAnkle = ([0., 0.])

            if MidAnkle[1] - MidHip[1] <= threshold:
                if count >= 20:
                    cv2.putText(frames[k], "Tumble", (int(frames[k].shape[0] / 5), int(frames[k].shape[1] / 5)), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 4)
                    count = 0
                else:
                    count += 1
                    cv2.putText(frames[k], "{}".format(n), (int(MidHip[0]), int(MidHip[1])), cv2.FONT_HERSHEY_PLAIN, 4, (255,0,0), 4)
            out.write(frames[k])

        if count >= 20:
            print('somebody tumbled!')

    out.release()
    cv2.destroyAllWindows()



def get_frames(video_path):
    video = cv2.VideoCapture(video_path)
    size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    frames=[]
    if video.isOpened()==False:
        print('Error opening video stream or file!')
    while(True):
        ret, frame=video.read()
        if ret is False:
            break
        frames.append(frame)
    video.release()
    return frames, size


if __name__=='__main__':
    video_path='data/fall.flv'
    json_dir='data/json/fall/sep-json'
    out_path='outputs/fall.mp4'
    threshold=20

    fall_video(video_path, json_dir, out_path, threshold)