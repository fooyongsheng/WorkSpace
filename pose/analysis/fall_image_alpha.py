import cv2
import os
import numpy as np

from utils.utils import get_keypoints


def fall_image(image_path, json_path, threshold):
    image=cv2.imread(image_path)
    keypoints=get_keypoints(json_path)

    for j in range(len(keypoints)):
        Rhip = keypoints[j][8]
        Lhip = keypoints[j][11]
        Rank = keypoints[j][10]
        Lank = keypoints[j][13]
        Neck = keypoints[j][1]

        MidHip = (Rhip + Lhip) / len(np.array([Rhip[1], Lhip[1]]).nonzero()[0])
        MidAnkle = (Rank + Lank) / len(np.array([Rank[1], Lank[1]]).nonzero()[0])

        if MidAnkle[1] - MidHip[1] <= threshold or MidHip[1] - Neck[1] <= threshold:
            cv2.circle(image, (int(MidHip[0]), int(MidHip[1])), 2, (255,0,0), 2)
            cv2.circle(image, (int(MidAnkle[0]), int(MidAnkle[1])), 2, (255,0,0), 2)
            cv2.circle(image, (int(Neck[0]), int(Neck[1])), 2, (255,0,0), 2)
            cv2.putText(image, "T", (int(MidHip[0]), int(MidHip[1])), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)

        cv2.imshow('image', image)
        cv2.waitKey(0)



if __name__=='__main__':
    image_path='data/4.jpg'
    json_path='data/json/4_keypoints.json'
    threshold=0.0

    fall_image(image_path, json_path, threshold)





