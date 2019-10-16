import os
import cv2


def image_resize(image):
    height=image.shape[0]
    width=image.shape[1]
    image=cv2.resize(image, (int(width/2), int(height/2)), interpolation=cv2.INTER_AREA)
    return image


def video2image(video_path, images_path):
    if not os.path.exists(images_path):
        os.mkdir(images_path)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError('can not open video')

    n=0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = image_resize(frame)
        image_path = '{}/{}.jpg'.format(images_path, n)
        cv2.imwrite(image_path, frame)
        n+=1
    cap.release()


def run_video2image():
    videos_path = '/home/yxq/datasets/migu/motion_list_full'
    name_list = os.listdir(videos_path)
    outs_path = '/home/yxq/datasets/migu/motion_list_images'

    for i in range(len(name_list)):
        video_path='{}/{}'.format(videos_path, name_list[i])
        name=video_path.split('.')[0].rsplit('/', 1)[-1]
        images_path='{}/{}'.format(outs_path, name)
        video2image(video_path, images_path)


def run_image_resize():
    images_path='/home/yxq/datasets/migu/motion_background1/images'
    images_list=os.listdir(images_path)

    images_save = '/home/yxq/datasets/migu/motion_background1/images2'
    if not os.path.exists(images_save):
        os.mkdir(images_save)

    for i in range(len(images_list)):
        image=cv2.imread('{}/{}'.format(images_path, images_list[i]))
        image=image_resize(image)
        cv2.imwrite('{}/{}.jpg'.format(images_save, images_list[i].split('.')[0]), image)

    print('resize finish!')


def run_imagedir_resize():
    images_dir_path='/home/yxq/datasets/migu/motion_background7'
    dir_names=os.listdir(images_dir_path)

    dir_save = '/home/yxq/datasets/migu/motion_background77'
    if not os.path.exists(dir_save):
        os.mkdir(dir_save)

    for i in range(len(dir_names)):
        images_list=os.listdir('{}/{}'.format(images_dir_path, dir_names[i]))
        images_save = '{}/{}'.format(dir_save, dir_names[i])
        if not os.path.exists(images_save):
            os.mkdir(images_save)

        for j in range(len(images_list)):
            image=cv2.imread('{}/{}/{}'.format(images_dir_path, dir_names[i], images_list[j]))
            image=image_resize(image)
            cv2.imwrite('{}/{}.jpg'.format(images_save, images_list[j].split('.')[0]), image)

        print('resize {} finish!'.format(dir_names[i]))


if __name__ == '__main__':
    run_video2image()
    # run_imagedir_resize()
