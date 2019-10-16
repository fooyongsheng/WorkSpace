#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

def access_pixels(img):
    '''遍历图像每个像素通道'''
    print(img.shape)   # h, w, c
    height=img.shape[0]
    width=img.shape[1]
    channels=img.shape[2]

    print(img.size)   #图像数组内总的元素数目,h*w*c
    for row in range(height):
        for col in range(width):
            for channel in range(channels):   #BGR
                if img[row][col][channel]==0:
                    img[row][col][channel]=230
                elif img[row][col][channel]==255:
                    img[row][col][channel]=0
    cv2.imshow('image', img)
    cv2.imwrite('out.png', img)




def create_img():
    img=np.zeros([660, 480, 3], dtype=np.uint8)
    img[:, :, :]=np.ones([660, 480, 3])*250

    point_color=(0, 0, 0)


    points=((240, 50), (240, 135), (170, 135), (150, 245), (130, 340), (310, 135), (330, 245), (350, 340), (190, 350),
            (180, 500), (180, 630), (290, 350), (300, 500), (300, 630), (220, 40), (260, 40), (200, 50), (280, 50))

    text_points=((250, 60), (250, 150), (150, 135), (130, 245), (110, 340), (320, 135), (340, 245), (360, 340), (170, 350),
            (160, 500), (150, 630), (300, 350), (310, 500), (310, 630), (210, 30), (260, 30), (170, 50), (300, 50))

    lines=((1, 2), (2, 3), (3, 4), (1, 5), (5, 6), (6, 7), (1, 0), (0, 14), (14, 16), (0, 15), (15, 17),
          (1, 8), (8, 9), (9, 10), (1, 11), (11, 12), (12, 13))

    for i in range(len(points)):
        cv2.circle(img, points[i], 2, point_color, 2)
        cv2.putText(img, str(i), text_points[i], cv2.FONT_HERSHEY_PLAIN, 1, point_color, 1)

    for i in range(len(lines)):
        line_color = np.random.randint(0, 255, size=(1, 3))
        line_color = (int(line_color[0][0]), int(line_color[0][1]), int(line_color[0][2]))
        cv2.line(img, points[lines[i][0]], points[lines[i][1]], line_color, 2)


    cv2.line(img, (10, points[4][1]), (470, points[4][1]), (0, 0, 0), 1)
    cv2.line(img, (points[4][0], 10), (points[4][0], 650), (0, 0, 0), 1)
    #cv2.putText(img, 'o', (points[4][0]+5, points[4][1]+15), cv2.FONT_HERSHEY_PLAIN, 1, point_color, 1)

    cv2.line(img, (10, points[4][1]), (15, points[4][1] - 5), (0, 0, 0), 1)
    cv2.line(img, (10, points[4][1]), (15, points[4][1] + 5), (0, 0, 0), 1)
    cv2.putText(img, 'L', (10, points[4][1]+15), cv2.FONT_HERSHEY_PLAIN, 1, point_color, 1)

    cv2.line(img, (465, points[4][1] - 5), (470, points[4][1]), (0, 0, 0), 1)
    cv2.line(img, (465, points[4][1] + 5), (470, points[4][1]), (0, 0, 0), 1)
    cv2.putText(img, 'R', (465, points[4][1]+15), cv2.FONT_HERSHEY_PLAIN, 1, point_color, 1)

    cv2.line(img, (points[4][0], 10), (points[4][0] + 5, 15), (0, 0, 0), 1)
    cv2.line(img, (points[4][0], 10), (points[4][0] - 5, 15), (0, 0, 0), 1)
    cv2.putText(img, 'U', (points[4][0]-15, 20), cv2.FONT_HERSHEY_PLAIN, 1, point_color, 1)

    cv2.line(img, (points[4][0], 650), (points[4][0] + 5, 645), (0, 0, 0), 1)
    cv2.line(img, (points[4][0], 650), (points[4][0] - 5, 645), (0, 0, 0), 1)
    cv2.putText(img, 'D',(points[4][0]-15, 650), cv2.FONT_HERSHEY_PLAIN, 1, point_color, 1)





    cv2.imshow('image', img)
    cv2.imwrite('draw.png', img)


def draw_coordinate_one():
    img = np.zeros([200, 200, 3], dtype=np.uint8)
    img[:, :, :] = np.ones([200, 200, 3]) * 250
    color = (0, 0, 0)
    color_line = (255, 0, 0)

    cv2.line(img, (10, 100), (190, 100), color, 1)
    cv2.line(img, (100, 10), (100, 190), color, 1)

    cv2.line(img, (190, 100), (185, 95), color, 1)
    cv2.line(img, (190, 100), (185, 105), color, 1)
    cv2.putText(img, 'x', (185, 115), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)


    cv2.line(img, (100, 190), (105, 185), color, 1)
    cv2.line(img, (100, 190), (95, 185), color, 1)
    cv2.putText(img, 'y', (105, 190), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)

    cv2.line(img, (100, 100), (170, 170), color_line, 1)

    cv2.circle(img, (120, 120), 1, color, 2)
    cv2.circle(img, (150, 150), 1, color, 2)

    cv2.putText(img, 'p1', (110, 135), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)
    cv2.putText(img, 'p2', (140, 165), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)

    cv2.ellipse(img, (100, 100), (28, 28), 0, 0, 45, (255, 0, 0), 1, 3)
    cv2.putText(img, 'a>0', (130, 120), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)

    cv2.imshow('image', img)
    cv2.imwrite('coordinate_1.png', img)



def draw_coordinate_two():
    img = np.zeros([200, 200, 3], dtype=np.uint8)
    img[:, :, :] = np.ones([200, 200, 3]) * 250
    color = (0, 0, 0)
    color_line = (255, 0, 0)

    #坐标
    cv2.line(img, (10, 100), (190, 100), color, 1)
    cv2.line(img, (100, 10), (100, 190), color, 1)

    #x箭头
    cv2.line(img, (190, 100), (185, 95), color, 1)
    cv2.line(img, (190, 100), (185, 105), color, 1)
    cv2.putText(img, 'x', (185, 115), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)

    #y箭头
    cv2.line(img, (100, 190), (105, 185), color, 1)
    cv2.line(img, (100, 190), (95, 185), color, 1)
    cv2.putText(img, 'y', (105, 190), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)

    #直线
    cv2.line(img, (100, 100), (30, 170), color_line, 1)

    #两点
    cv2.circle(img, (80, 120), 1, color, 2)
    cv2.circle(img, (50, 150), 1, color, 2)
    cv2.putText(img, 'p1', (80, 130), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)
    cv2.putText(img, 'p2', (50, 160), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)

    #弧线
    cv2.ellipse(img, (100, 100), (28, 28), 0, 0, 135, (255, 0, 0), 1, 3)
    cv2.putText(img, 'a>0', (110, 135), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)

    cv2.imshow('image', img)
    cv2.imwrite('coordinate_2.png', img)


def draw_coordinate_three():
    img = np.zeros([200, 200, 3], dtype=np.uint8)
    img[:, :, :] = np.ones([200, 200, 3]) * 250
    color = (0, 0, 0)
    color_line = (255, 0, 0)

    #坐标
    cv2.line(img, (10, 100), (190, 100), color, 1)
    cv2.line(img, (100, 10), (100, 190), color, 1)

    #x箭头
    cv2.line(img, (190, 100), (185, 95), color, 1)
    cv2.line(img, (190, 100), (185, 105), color, 1)
    cv2.putText(img, 'x', (185, 115), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)

    #y箭头
    cv2.line(img, (100, 190), (105, 185), color, 1)
    cv2.line(img, (100, 190), (95, 185), color, 1)
    cv2.putText(img, 'y', (105, 190), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)

    #直线
    cv2.line(img, (100, 100), (30, 30), color_line, 1)

    #两点
    cv2.circle(img, (80, 80), 1, color, 2)
    cv2.circle(img, (50, 50), 1, color, 2)
    cv2.putText(img, 'p1', (82, 80), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)
    cv2.putText(img, 'p2', (55, 50), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)

    #弧线
    cv2.ellipse(img, (100, 100), (28, 28), 225, 0, 135, (255, 0, 0), 1, 3)
    cv2.putText(img, 'a<0', (110, 70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)

    cv2.imshow('image', img)
    cv2.imwrite('coordinate_3.png', img)


def draw_coordinate_four():
    img = np.zeros([200, 200, 3], dtype=np.uint8)
    img[:, :, :] = np.ones([200, 200, 3]) * 250
    color = (0, 0, 0)
    color_line = (255, 0, 0)

    #坐标
    cv2.line(img, (10, 100), (190, 100), color, 1)
    cv2.line(img, (100, 10), (100, 190), color, 1)

    #x箭头
    cv2.line(img, (190, 100), (185, 95), color, 1)
    cv2.line(img, (190, 100), (185, 105), color, 1)
    cv2.putText(img, 'x', (185, 115), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)

    #y箭头
    cv2.line(img, (100, 190), (105, 185), color, 1)
    cv2.line(img, (100, 190), (95, 185), color, 1)
    cv2.putText(img, 'y', (105, 190), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)

    #直线
    cv2.line(img, (100, 100), (170, 30), color_line, 1)

    #两点
    cv2.circle(img, (120, 80), 1, color, 2)
    cv2.circle(img, (150, 50), 1, color, 2)
    cv2.putText(img, 'p1', (125, 80), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)
    cv2.putText(img, 'p2', (155, 50), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)

    #弧线
    cv2.ellipse(img, (100, 100), (28, 28), 315, 0, 45, (255, 0, 0), 1, 3)
    cv2.putText(img, 'a<0', (130, 95), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)

    cv2.imshow('image', img)
    cv2.imwrite('coordinate_4.png', img)




# img=cv2.imread('keypoints_pose_18.png')
# access_pixels(img)


# create_img()
draw_coordinate_four()

cv2.waitKey(0)
cv2.destroyAllWindows()



# import turtle
# turtle.left(45)
# turtle.circle(50, 45)
# turtle.done()
