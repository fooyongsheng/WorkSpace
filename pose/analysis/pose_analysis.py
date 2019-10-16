import json
import numpy as np
import math
import cv2


def HandCenter(json_path, confidence):
    '''
    :param json_path: the path of a json file
    :param confidence: if confidence larger than confidence, we think it is a real point, otherwise
    :return: the center points of two hands: (hand_left_x, hand_left_y, hand_right_x, hand_right_y)
    '''
    json_file=open(json_path, encoding='utf-8')
    jsons=json_file.read()

    dicts=json.loads(jsons)
    people=dicts['people']
    handCenters=[]

    for p in range(len(people)):
        hand_left=people[p]['hand_left_keypoints_2d']
        hand_right=people[p]['hand_right_keypoints_2d']

        hand_left=np.array(hand_left).reshape(-1, 3)   # reshape to 21*3, 3 represents (x, y, confidence)
        hand_right=np.array(hand_right).reshape(-1, 3)

        #compute the left hand center points
        count_left=0
        sum_left_x, sum_left_y=0.0, 0.0
        for i in range(len(hand_left)):
            if hand_left[i][2]>=confidence:
                count_left += 1
                sum_left_x += hand_left[i][0]
                sum_left_y += hand_left[i][1]
        if sum_left_x>0 and sum_left_y>0 and count_left>0:
            hand_left_x=sum_left_x/count_left
            hand_left_y=sum_left_y/count_left
        else:  # the left hand is unvisible
            hand_left_x=0.0
            hand_left_y=0.0

        # compute the right hand center points
        count_right = 0
        sum_right_x, sum_right_y= 0.0, 0.0
        for i in range(len(hand_right)):
            if hand_right[i][2] >= confidence:
                count_right += 1
                sum_right_x += hand_right[i][0]
                sum_right_y += hand_right[i][1]
        if sum_right_x > 0 and sum_right_y > 0 and count_right > 0:
            hand_right_x = sum_right_x / count_right
            hand_right_y = sum_right_y / count_right
        else:  # the right hand is unvisible
            hand_right_x=0.0
            hand_right_y=0.0

        # put the hand center points together
        handCenters.append([int(hand_left_x), int(hand_left_y), int(hand_right_x), int(hand_right_y)])
    return handCenters


def Angle(vertices, direction, image):
    '''
    :param vertices: the vertices used to calculate the angle
    :param direction: U(upward), D(downward), L(left), R(right)
    H(horizon, obtuse angle), h(horizon, acute angle), V(vertical, obtuse angle), v(vertical, acute angle)
    :param image_path: image path, in order to get the width and height of image
    :return: the angle in a given direction
    '''

    # one way to compute angle: UDLR
    if direction=='U' or direction=='u':   #the angle in the upward direction
        if vertices[0]<vertices[2]:
            dx=vertices[2]-vertices[0]
            dy=vertices[3]-vertices[1]
            cross_x=vertices[0]
            cross_y=vertices[1]
        else:
            dx=vertices[0]-vertices[2]
            dy=vertices[1]-vertices[3]
            cross_x=vertices[2]
            cross_y=vertices[3]
        angle=math.atan2(dx,dy)
        angle=int(angle*180/math.pi)
        angle=180-abs(angle)
        length=0
        axis=(cross_x, cross_y, cross_x, length)

    if direction=='D' or direction=='d':    #the angle in the downward direction
        if vertices[0]<vertices[2]:
            dx=vertices[2]-vertices[0]
            dy=vertices[3]-vertices[1]
            cross_x=vertices[0]
            cross_y=vertices[1]
        else:
            dx=vertices[0]-vertices[2]
            dy=vertices[1]-vertices[3]
            cross_x=vertices[2]
            cross_y=vertices[3]
        angle=math.atan2(dx,dy)
        angle=int(angle*180/math.pi)
        angle=abs(angle)
        length=len(image[0])
        axis=(cross_x, cross_y, cross_x, length)

    if direction=='L' or direction=='l':    #the angle in the left direction
        if vertices[1]<vertices[3]:
            dx=vertices[2]-vertices[0]
            dy=vertices[3]-vertices[1]
            cross_x=vertices[2]
            cross_y=vertices[3]
        else:
            dx=vertices[0]-vertices[2]
            dy=vertices[1]-vertices[3]
            cross_x=vertices[0]
            cross_y=vertices[1]
        angle=math.atan2(dy,dx)
        angle=int(angle*180/math.pi)
        angle=abs(angle)
        length=0
        axis=(cross_x, cross_y, length, cross_y)

    if direction=='R' or direction=='r':    #the angle in the right direction
        if vertices[1]<vertices[3]:
            dx=vertices[2]-vertices[0]
            dy=vertices[3]-vertices[1]
            cross_x=vertices[2]
            cross_y=vertices[3]
        else:
            dx=vertices[0]-vertices[2]
            dy=vertices[1]-vertices[3]
            cross_x=vertices[0]
            cross_y=vertices[1]
        angle=math.atan2(dy,dx)
        angle=int(angle*180/math.pi)
        angle=180-abs(angle)
        length=len(image[1])
        axis=(cross_x, cross_y, length, cross_y)

    # another way to compute angle: HhVv
    if direction=='H' or direction=='h':    # horizon, H:obtuse angle, h:acute angle
        if vertices[1] < vertices[3]:
            dx = vertices[2] - vertices[0]
            dy = vertices[3] - vertices[1]
            cross_x = vertices[2]
            cross_y = vertices[3]
        else:
            dx = vertices[0] - vertices[2]
            dy = vertices[1] - vertices[3]
            cross_x = vertices[0]
            cross_y = vertices[1]
        angle = math.atan2(dy, dx)
        angle = int(angle * 180 / math.pi)
        if direction=='H':
            if abs(angle)>=90:
                angle=abs(angle)
                length = 0
            else:
                angle=180-abs(angle)
                length=len(image[1])
        elif direction=='h':
            if abs(angle)<=90:
                angle=abs(angle)
                length=0
            else:
                angle=180-abs(angle)
                length=len(image[1])
        axis = (cross_x, cross_y, length, cross_y)

    if direction=='V' or direction=='v':  # vertical, V:obtuse angle, v:acute angle
        if vertices[0] < vertices[2]:
            dx = vertices[2] - vertices[0]
            dy = vertices[3] - vertices[1]
            cross_x = vertices[0]
            cross_y = vertices[1]
        else:
            dx = vertices[0] - vertices[2]
            dy = vertices[1] - vertices[3]
            cross_x = vertices[2]
            cross_y = vertices[3]
        angle = math.atan2(dx, dy)
        angle = int(angle * 180 / math.pi)
        if direction=='V':
            if abs(angle)>=90:
                angle = abs(angle)
                length = len(image[0])
            else:
                angle = 180 - abs(angle)
                length = 0
        elif direction=='v':
            if abs(angle)<=90:
                angle=abs(angle)
                length=len(image[0])
            else:
                angle=180-abs(angle)
                length=0
        axis = (cross_x, cross_y, cross_x, length)

    return angle, axis



def HeadCenter(json_path, confidence):
    json_file=open(json_path, encoding='utf-8')
    jsons=json_file.read()

    dicts=json.loads(jsons)
    people=dicts['people']
    headCenters=[]

    for p in range(len(people)):
        pose=people[p]['pose_keypoints_2d']
        pose=np.array(pose).reshape(-1, 3)    #25*3, 3:(x, y, confidence)

        Nose=pose[0]
        REye=pose[15]
        LEye=pose[16]

        if REye[0]!=0 and REye[1]!=0 and LEye[0]!=0 and LEye[1]!=0:
            headcenter_x = (REye[0] + LEye[0]) / 2.0
            headcenter_y = (REye[1] + LEye[1]) / 2.0
            confidence = (REye[2] + LEye[2]) / 2.0
        elif REye[0]!=0 and REye[1]!=0:
            headcenter_x=REye[0]
            headcenter_y=REye[1]
            confidence=REye[2]
        elif LEye[0]!=0 and LEye[1]!=0:
            headcenter_x=LEye[0]
            headcenter_y=LEye[1]
            confidence=LEye[2]
        else:
            headcenter_x=Nose[0]
            headcenter_y=Nose[1]
            confidence=Nose[2]

        # put the head center points together
        headCenters.append([int(headcenter_x), int(headcenter_y)])
        return headCenters



def ShowPoint():
    json_path = '../Json/TumbleImg_json/17_keypoints.json'
    image_path='../Data_row/TumbleImg/17.jpg'
    confidence = 0.0
    point_size = 1
    point_color = (0, 0, 255)
    thickness = 1

    img=cv2.imread(image_path)
    kps = ReadPose(json_path, confidence)

    point = []
    points=[]
    for j in range(len(kps)):    #the number of people
        for i in range(len(kps[j])):   #the number of key points
            point.append((int(kps[j][i][0]), int(kps[j][i][1])))
        points.append(point)


    for j in range(len(points)):   #the number of people
        k = 0   # flag the label of number
        for pt in points[j]:
            cv2.circle(img, pt, point_size, point_color, thickness)
            cv2.putText(img, str(k), pt, cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
            k += 1

    cv2.imshow('img', img)
    cv2.waitKey(0)


def ReadPose(json_path, confidence):
    '''
    the keypoints ordering is openpose COCO-18 or POSE-25
    :param json_path:
    :param confidence:
    :return:
    '''
    json_file=open(json_path, encoding='utf-8')
    jsons = json_file.read()

    dicts = json.loads(jsons)
    people = dicts['people']

    kps=[]
    for p in range(len(people)):
        kp=people[p]['pose_keypoints_2d']
        kp=np.array(kp).reshape(-1, 3)
        kps.append(kp)

    return kps




if __name__=='__main__':
    json_path = '../Json/TumbleImg_json/17_keypoints.json'
    confidence=0.0

    #headCenters=HeadCenter(json_path, confidence)
    # kps=ReadPose(json_path, confidence)
    # print(len(kps[0]))

    ShowPoint()














