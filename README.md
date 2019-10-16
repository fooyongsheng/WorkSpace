### WorkSpace

对所做的项目做一些简单的记录和描述。

##### 人流估计和人体摔倒检测

​	主要使用的是[darknet](https://pjreddie.com/darknet/yolo/)模型，首先检测出目标中的人体，就可以进行人流估计，人体摔倒主要是对检测出的人体bounding box进行一些约束判断，从而判断这个人是否摔倒。

​	在darknet源码上增加自己的代码，代码detection/fall_detector.py, flow_detector.py, webcam_fall_detector.py，输入都是视频，本地或在线视频。运行代码时，需要根据自己的路径修改darknet/python/darknet.py中libdarknet.so的路径。

##### 人体姿态估计

 1. 数据集处理，原始数据集是视频，每个视频代表一类动作

    ​	（1）将视频转换为图片，每个视频作为一个文件夹类，代码pose/datasets/videos_to_images.py，不依赖环境，为了运行速度快，可以同时跑几个进程。

    ​	（2）给白色背景的视频添加背景，代码pose/datasets/background_change.py，不依赖环境。

    ​	（3）视频批量处理提取人体骨架，代码pose/datasets/videos_keypoints.py，依赖[openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)环境。

    ​	（4）多文件夹图像批量提取人体骨架，代码pose/datasets/images_keypoints.py，依赖[openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)环境。

    ​	（5）删除重名文件夹，代码pose/datasets/directory_remove.py，不依赖环境。

    ​	（6）将图像id和关键点json文件的id对齐，代码pose/datasets/img_kp_alignment.py，不依赖环境。

    ​	（7）如果需要检测人体bounding box，代码pose/datasets/images_bbox.py，依赖[darknet](https://pjreddie.com/darknet/yolo/)环境。

    ​	（8）生成类似COCO数据集的标注形式，代码pose/datasets/json_create.py，不依赖环境。

 2. 皮划艇动作姿态分析

    ​	（1）对openpose模型和alphapose(采用openpose的json保存格式)模型提取处理的关键点文件解析，代码pose/analysis/pose_analysis.py，需要先利用关键点检测模型得到关键点的json文件，依赖[openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)环境或者[alphapose](https://github.com/MVIG-SJTU/AlphaPose)环境。

    ​	（2）解析m3u8格式的在线视频，代码pose/analysis/m3u8_analysis.py，不依赖环境。

    ​	（3）手动绘制骨架图，绘制坐标图，代码pose/analysis/draw_skeleton.py，不依赖环境。

    ​	（4）利用关键点判断图像中人体摔倒，不依赖环境，前期使用openpose提取关键点，代码pose/analysis/fall_images.py；前期使用alphapose提取关键点，代码pose/analysis/fall_images_alpha.py

    ​	（5）利用关键点判断视频中人体摔倒，不依赖环境，前期使用openpose提取关键点，代码pose/analysis/fall_video.py；前期使用alphapose提取关键点，代码pose/analysis/fall_video_alpha.py。

    ​	（6）皮划艇动作分析，计算图像中关节角度，代码pose/analysis/kayak_image.py，不依赖环境，前期需要使用openpose提取关键点。

    ​	（7）皮划艇动作分析，计算视频中关节角度，代码pose/analysis/kayak_video.py，不依赖环境，前期需要使用openpose提取关键点。

##### 使用darknet训练自己的数据集

​	[darknet](https://pjreddie.com/darknet/yolo/)适用的训练数据模型有voc和coco，通常用voc会相对简单一点，使用自己的数据集训练时候

​		(1) 将自己的数据转换为voc格式，通常数据集下面有两个文件夹Annotations和JPEGImages，前者存放bounding box的标注数据xml文件，后者是原始图像文件。运行代码detection/train_voc/voc_utils.py，在该路径下得到共6个文件，包括训练集和测试集。

​		(2) 如果标注数据不规范，使用detection/train_voc/xml_process.py进行处理。

​		(3) 修改detection/train_voc/voc.data, voc.names, yolov3-voc.cfg，注意cfg文件中，训练和测试时候的batch和subdivisions参数的变化，网络最后的输出层中filters要更加类别做修改，filters=(5+numclass)*3. 



