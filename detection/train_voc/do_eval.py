from voc_eval import voc_eval


detpath='/home/yxq/Projects/darknet/results/comp4_det_test_Baby carriage.txt'
annopath='/home/yxq/Projects/darknet/dataset_yxq/Baby_carriage/Annotations/{}.xml'
imagesetfile='/home/yxq/Projects/darknet/dataset_yxq/Baby_carriage/ImageSets/Main/test.txt'
classname=('Baby carriage')
cachedir='/home/yxq/Projects/darknet/dataset_yxq/'

rec, prec, ap=voc_eval(detpath, annopath, imagesetfile, classname, cachedir, ovthresh=0, use_07_metric=False)

print('rec:', rec)
print('prec:', prec)
print('ap:', ap)
























