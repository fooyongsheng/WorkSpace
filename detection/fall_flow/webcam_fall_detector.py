# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

#_*_coding:UTF-8_*_
#coding=utf-8

import sys, os
sys.path.append(os.path.join(os.getcwd(),'python/'))
import cv2
from timeit import default_timer as timer

import darknet as dn


dn.set_gpu(0)
net = dn.load_net("cfg/yolov3.cfg", "weights/yolov3.weights", 0)
meta = dn.load_meta("cfg/coco.data")

def fall_image(image_path):
    FALL=False
    number=0
    start_time=timer()
    res = dn.detect(net, meta, image_path, thresh=.5, hier_thresh=.5, nms=.45)

    if len(res)>0:
        for i in range(len(res)):
            if res[i][0]=='person':
                number += 1
                # print(res[i])
                if res[i][1]>=0.5:
			box=res[i][2]
			if box[2] >= (1.3*box[3]):   
                            FALL=True
                    # print('somebody fall!')

    end_time=timer()
    fps = 1.0 / (end_time - start_time)
    # print('time:', end_time - start_time)
    # print('fps:', fps)
    return FALL, number

def h264_pc_rtsp_src(url):
    return 'rtspsrc location={} latency=0 ! rtph264depay ! h264parse ! queue ! avdec_h264 ! videoconvert ! appsink'.format(url)



def fall_video(video_path, output_path=""):

    #video_path = h264_pc_rtsp_src(video_path)
    print('address:',video_path)
    cap=cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise IOError('could not open webcam or video')
    video_fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
    video_fps=cap.get(cv2.CAP_PROP_FPS)
    video_size=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    out = cv2.VideoWriter(output_path, video_fourcc, video_fps, video_size)

    count=0
    while True:
        ret, frame=cap.read()
        if not ret:
            print('error or finished!')
            break
        # print(frame.shape)
        start_time=timer()
        cv2.imwrite('data/fall/tmp.jpg', frame)
        FALL, number=fall_image(b'data/fall/tmp.jpg')
        end_time=timer()
        exec_time=end_time-start_time
        fps=1.0/exec_time

        cv2.putText(frame, 'fps:{:.1f}'.format(fps), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        cv2.putText(frame, 'people:{}'.format(number), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
        if FALL and count < 10:
            count += 1
        if count >= 10:
            cv2.putText(frame, 'somebody fall!', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            count += 1
        if count >= 30:
            count = 0
        cv2.namedWindow('result', cv2.WINDOW_NORMAL)
        out.write(frame)
        cv2.imshow('result', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image_path=b'data/fall/person.jpg'
    #video_path = 'data/fall/fall.flv'
    #output_path = 'data/fall/out.mp4'
    video_path='rtsp://admin:bsoft123@10.0.4.77/h264/chl/main/av_stream'


    # fall_image(image_path)
    fall_video(video_path, output_path='')





