# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

import sys, os
sys.path.append(os.path.join(os.getcwd(),'python/'))
import cv2
from timeit import default_timer as timer
import urllib.request
import requests

import darknet as dn


dn.set_gpu(0)
net = dn.load_net(b"cfg/yolov3.cfg", b"weights/yolov3.weights", 0)
meta = dn.load_meta(b"cfg/coco.data")

def flow_image(image_path):
    number = 0
    start_time=timer()
    res = dn.detect(net, meta, image_path, thresh=.5, hier_thresh=.5, nms=.45)

    if len(res)>0:
        for i in range(len(res)):
            if res[i][0]==b'person' and res[i][1]>=0.0:
                # print(res[i])
                number += 1

    end_time=timer()
    fps = 1.0 / (end_time - start_time)
    print('time:', end_time - start_time)
    print('fps:', fps)
    return number

def flow_video(video_path, output_path=""):
    cap=cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError('could not open webcam or video')
    # video_fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
    video_fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_fps=cap.get(cv2.CAP_PROP_FPS)
    video_size=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    out = cv2.VideoWriter(output_path, video_fourcc, video_fps, video_size)

    while True:
        ret, frame=cap.read()
        if not ret:
            print('error or finished!')
            break
        # print(frame.shape)
        start_time=timer()
        cv2.imwrite('data/fall/tmp.jpg', frame)
        number=flow_image(b'data/fall/tmp.jpg')
        end_time=timer()
        exec_time=end_time-start_time
        fps=1.0/exec_time

        cv2.putText(frame, 'fps:{:.1f}'.format(fps), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        cv2.putText(frame, 'number:{}'.format(number), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

        cv2.namedWindow('result', cv2.WINDOW_NORMAL)
        out.write(frame)
        cv2.imshow('result', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def flow_webcam(m3u8_url, header):
    cap_list=[]
    cache_path='data/cache'
    if not os.path.exists(cache_path):
        os.mkdir(cache_path)
    while True:
        contents = requests.get(m3u8_url).text
        lines = contents.splitlines()

        if lines[0] != '#EXTM3U':
            raise BaseException(u'非M3U8的链接')
        else:
            for index, line in enumerate(lines):
                if 'EXTINF' in line:
                    pd_url = m3u8_url.rsplit('/', 1)[0] + '/' + lines[index + 1]
                    request = urllib.request.Request(pd_url, headers=header)
                    response = urllib.request.urlopen(request)

                    video = response.read()
                    file_name = lines[index + 1].split('/')[-1]
                    file_name = file_name.split('-')[-1]
                    print(file_name)

                    if file_name == '404_0.ts':
                        print('离线！！！')
                        continue

                    video_path = cache_path + '/' + file_name
                    with open(video_path, 'wb') as f:
                        f.write(video)
                        f.flush()

                    if file_name not in cap_list:
                        cap_list.append(file_name)
                        flow_video(video_path)
                    else:
                        continue
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image_path=b'data/fall/person.jpg'
    video_path = 'data/fall/fall.flv'
    output_path = 'data/fall/out.avi'
    m3u8_url='http://122.193.18.111:83/pag/172.22.71.2/7302/002499/0/SUB/TCP/live.m3u8'
    header = {'User-Agent': 'Mozilla/5.0 (Ubuntu NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


    # flow_image(image_path)
    # flow_video(video_path, output_path)
    flow_webcam(m3u8_url, header)





