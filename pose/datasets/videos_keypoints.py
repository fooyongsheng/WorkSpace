import os

videos_in_path='/media/Others/dataset_yxq/migu/motion_list_full'
videos_list=os.listdir(videos_in_path)

videos_out_path='/media/Others/dataset_yxq/migu/motion_list_keypoints'
if not os.path.exists(videos_out_path):
    os.mkdir(videos_out_path)


for i in range(len(videos_list)):
    video_in_path='{}/{}'.format(videos_in_path, videos_list[i])
    video_out_path='{}/{}/{}'.format(videos_out_path, videos_list[i].split('.')[0], videos_list[i])
    json_out_path='{}/{}/'.format(videos_out_path, videos_list[i].split('.')[0])

    cmd='./build/examples/openpose/openpose.bin --video {} --write_video {} --write_json {} --num_gpu 1 --num_gpu_start 0'.format(
        video_in_path, video_out_path, json_out_path)

    os.system(cmd)




