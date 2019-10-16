import json
import numpy as np
import cv2

def read_keypoints(json_path):
    json_file = open(json_path, encoding='utf-8')
    jsons = json_file.read()

    dicts = json.loads(jsons)
    people = dicts['people']

    multi_keypoints = []
    for p in range(len(people)):   # for multiple people
        kps = people[p]['pose_keypoints_2d']
        kps = np.array(kps).reshape(-1, 3)
        multi_keypoints.append(kps)
    return multi_keypoints


def create_info():
    info = {
        'description': 'motion dataset',
        'url': '',
        'version': '1.0',
        'year': '2019',
        'contributor': '',
        'data_created': '2019/10/08'
    }
    return info


def create_images(images_path, images_list):
    images_dict=[]
    for i in range(len(images_list)):
        image=cv2.imread('{}/{}'.format(images_path, images_list[i]))
        file_name=images_list[i]
        height=image.shape[0]
        width=image.shape[1]
        num=file_name.split('.')[0].lstrip('0')
        id=num if num!='' else '0'

        image_dict={
            'license':1,
            'file_name':file_name,
            'coco_url':'',
            'height':height,
            'width':width,
            'data_captured':'2019-10-10',
            'flickr_url':'',
            'id':id
        }
        images_dict.append(image_dict)

        print(images_dict)
        return images_dict




def create_person_keypoints(json_path, info):

    person_keypoints={
        'info':info,
        'licenses':'',

    }

    # json_str=json.dumps(person_keypoints)

    with open(json_path, 'w') as f:
        json.dump(person_keypoints, f)


if __name__ == '__main__':
    pass