import cv2
import os
from utils.utils import HandCenter, Angle


def images_process(image_dir, json_dir, out_dir):
    '''
    processing batch images
    :param image_dir:
    :param json_dir:
    :param out_dir:
    :return:
    '''
    confidence = 0.0
    direction = 'l'
    color = (255, 0, 0)

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    image_list=os.listdir(image_dir)
    json_list=os.listdir(json_dir)

    image_list_sort=[]
    for img in image_list:
        img_num=img.split('_')[1].split('.')[0]
        image_list_sort.append(int(img_num))
        image_list_sort.sort()

    json_list_sort=[]
    for js in json_list:
        js_num=js.split('_')[1]
        json_list_sort.append(int(js_num))
        json_list_sort.sort()

    for img, js in zip(image_list_sort, json_list_sort):
        img='image_{}.png'.format(img)
        js='image_{}_keypoints.json'.format(js)
        json_path='{}\{}'.format(json_dir, js)
        image_path='{}\{}'.format(image_dir, img)

        handCenters = HandCenter(json_path, confidence)
        vertices = handCenters[0]
        image=cv2.imread(image_path)
        angle, axis = Angle(vertices, direction, image)

        cv2.line(image, (vertices[0], vertices[1]), (vertices[2], vertices[3]), color, 2)
        cv2.line(image, (axis[0], axis[1]), (axis[2], axis[3]), color, 2)
        cv2.putText(image, "angle:" + str(angle), (axis[0], axis[1]), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)
        out_path='{}\{}'.format(out_dir, img)
        cv2.imwrite(out_path, image)

    print('Finished! You can check the output images on {}'.format(out_dir))


def image_process(image_path, json_path, out_path):
    '''
    processing single image
    :return:
    '''
    confidence = 0.0
    direction = 'h'
    color = (255, 0, 0)

    image=cv2.imread(image_path)
    handCenters = HandCenter(json_path, confidence)
    vertices = handCenters[0]
    angle, axis = Angle(vertices, direction, image)

    cv2.line(image, (vertices[0], vertices[1]), (vertices[2], vertices[3]), color, 2)
    cv2.line(image, (axis[0], axis[1]), (axis[2], axis[3]), color, 2)
    cv2.putText(image, "angle:"+str(angle), (axis[0], axis[1]), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

    cv2.imshow('image', image)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        print("Press 's' to save the result!")
    elif k == ord('s'):
        cv2.imwrite(out_path, image)
        cv2.destroyAllWindows()
        print('Finished! You can check the output image on {}'.format(out_dir))





if __name__=='__main__':
    image_dir='Data_row\Images'
    json_dir='Json\Images'
    out_dir='Result\Images'
    #images_process(image_dir, json_dir, out_dir)

    image_path = 'Data_row\Images\image_9.png'
    json_path = 'Json\Images\image_9_keypoints.json'
    out_path='Result\output.png'
    image_process(image_path, json_path, out_path)

