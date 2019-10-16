import os

images_dir_path='/media/Others/dataset_yxq/migu/motion_images'
dir_lists=os.listdir(images_dir_path)

keypoints_img_save='/media/Others/dataset_yxq/migu/motion_keypoints'
if not os.path.exists(keypoints_img_save):
    os.mkdir(keypoints_img_save)

keypoints_js_save='/media/Others/dataset_yxq/migu/motion_kpjson'
if not os.path.exists(keypoints_js_save):
    os.mkdir(keypoints_js_save)

for i in range(len(dir_lists)):
    imgs_in='{}/{}/'.format(images_dir_path, dir_lists[i])

    imgs_save='{}/{}'.format(keypoints_img_save, dir_lists[i])
    if not os.path.exists(imgs_save):
        os.mkdir(imgs_save)

    json_save='{}/{}'.format(keypoints_js_save, dir_lists[i])
    if not os.path.exists(json_save):
        os.mkdir(json_save)

    cmd='./build/examples/openpose/openpose.bin --image_dir {} --write_images {} ' \
        '--write_json {} --num_gpu 1 --num_gpu_start 0'.format(imgs_in, imgs_save, json_save)
    os.system(cmd)


