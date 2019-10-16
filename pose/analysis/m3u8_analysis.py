import os
import requests
import cv2

'''
m3u8是苹果公司推出的一种视频播放标准，是m3u的一种，不过编码方式是utf-8，是一种文本检索格式，将视频切割成小段的ts格式的视频文件，
然后存在服务器中(为了减少I/O访问次数，一般存在服务器的内存中)，通过m3u8解析出来路径，然后去请求。
.m3u8文件中，.ts后缀的文件地址是有规律的，只需要下载所有的.ts后缀文件，然后把它们整合成一个文件即可。
'''
'''
解析m3u8地址,获取.ts格式的视频文件,并计算人流.
下载m3u8文件里面的所有.ts片段, 每个m3u8文件中包含3个ts文件'''
def download(url):
    download_path=os.getcwd()+'/download'
    print(download_path)
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    all_content=requests.get(url).text   #获取m3u8的文件内容
    file_line=all_content.split('\r\n')  #读取文件里的每一行

    # for i in range(len(file_line)):
    #     print(file_line[i])

    #通过判断文件头来确定是否是m3u8文件
    if file_line[0] != '#EXTM3U':
        raise BaseException(u'非m3u8的链接')
    else:
        unknown=True     #用来判断是否找到了下载地址
        for index, line in enumerate(file_line):
            if 'EXTINF' in line:
                unknown=False
                #拼出ts片段的url
                pd_url=url.rsplit('/', 1)[0] + '/' + file_line[index + 1]    # rsplit(分隔符,分割几次),从右向左
                print(pd_url)
                res=requests.get(pd_url)
                print(res)
                c_fule_name=str(file_line[index + 1])

                with open(download_path +  '/' + c_fule_name, 'ab') as f:
                    f.write(res.content)
                    f.flush()

                videoCapture = cv2.VideoCapture(download_path + '/' + c_fule_name)
                fps=videoCapture.get(cv2.CAP_PROP_FPS)
                #size=(int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                #     int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
                #fNUMS=videoCapture.get(cv2.CAP_PROP_FRAM_COUNT)

                res,frame=videoCapture.read()
                while res:
                    cv2.imshow('windows', frame)
                    cv2.waitKey(int(1000/int(fps)))
                    res, frame=videoCapture.read()
                videoCapture.release()



        if unknown:
            raise BaseException('未找到对应的下载链接')
        else:
            print(u'下载完成')




if __name__=='__main__':
    download('http://122.193.18.111:83/pag/172.22.71.2/7302/002310/0/SUB/TCP/live.m3u8')










