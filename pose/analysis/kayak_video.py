import os
import cv2
from utils.utils import HandCenter, Angle, HeadCenter


def video_process(video_path, json_dir, out_path):
    confidence = 0.0
    direction = 'R'
    color = (255, 0, 0)
    n = 0

    frames=cv2.VideoCapture(video_path)
    json_list = os.listdir(json_dir)
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    size=(int(frames.get(cv2.CAP_PROP_FRAME_WIDTH)), int(frames.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out=cv2.VideoWriter(out_path, fourcc, 10.0, size)

    if frames.isOpened()==False:
        print('Error opening video stream or file!')
    while(True):
        ret, frame=frames.read()

        if ret is False:
            break
        json_path='{}\{}'.format(json_dir,json_list[n])
        #print(json_path)
        n += 1

        handCenters = HandCenter(json_path, confidence)
        #print(handCenters[0])
        vertices = handCenters[0]
        angle, axis = Angle(vertices, direction, frame)

        headCenters = HeadCenter(json_path, confidence)
        head=headCenters[0]


        cv2.line(frame, (vertices[0], vertices[1]), (vertices[2], vertices[3]), color, 2)
        cv2.line(frame, (axis[0], axis[1]), (axis[2], axis[3]), color, 2)
        cv2.line(frame, (head[0]-500, head[1]), (head[0]+500, head[1]), color, 2)
        cv2.putText(frame, "angle:" + str(angle), (axis[0], axis[1]), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

        out.write(frame)

    print('Finished! You can check the output video on {}'.format(out_path))
    frames.release()
    out.release()
    cv2.destroyAllWindows()


if __name__=='__main__':
    video_path = 'Data_row\Videos\\video5.mp4'
    json_dir = 'Json\\video5'
    out_path = 'Result\Videos\\video5.avi'

    video_process(video_path, json_dir, out_path)



