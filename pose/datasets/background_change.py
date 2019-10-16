import os
import cv2


def add_background(foreground, background):
    height=foreground.shape[0]
    widht=foreground.shape[1]
    channels=foreground.shape[2]

    for row in range(height):
        for col in range(widht):
            for channel in range(channels):
                if foreground[row][col][channel]<250:
                    background[row][col][channel]=foreground[row][col][channel]
                else:
                    continue
    return background


def run_add_background():
    images_in_path = '/home/yxq/datasets/migu/motion_images1'
    images_list = os.listdir(images_in_path)

    bgs_in_path='/home/yxq/datasets/migu/background1'
    bgs_list=os.listdir(bgs_in_path)

    images_out_path = '/home/yxq/datasets/migu/motion_background1'
    if not os.path.exists(images_out_path):
        os.mkdir(images_out_path)

    for i in range(len(bgs_list)):
        bg_path='{}/{}'.format(bgs_in_path, bgs_list[i])

        for j in range(len(images_list)):
            images_path='{}/{}'.format(images_in_path, images_list[j])
            images=os.listdir(images_path)

            output_path = '{}/{}_{}'.format(images_out_path, images_list[j].split('.')[0], bgs_list[i].split('.')[0])
            if not os.path.exists(output_path):
                os.mkdir(output_path)

            for k in range(len(images)):
                background = cv2.imread(bg_path)
                # cv2.imshow('background', background)
                # cv2.waitKey(5)
                image_path='{}/{}'.format(images_path, images[k])
                foreground=cv2.imread(image_path)
                # cv2.imshow('foreground', foreground)
                # cv2.waitKey(5)
                background=cv2.resize(background, (foreground.shape[1], foreground.shape[0]), interpolation=cv2.INTER_AREA)
                result=add_background(foreground, background)
                image_out_path = '{}/{}'.format(output_path, images[k])
                # print(image_out_path)
                cv2.imwrite(image_out_path, result)
        print('finish one images file!')


if __name__ == '__main__':
    run_add_background()

    print('finish!')







