import cv2, os, shutil
import xml.etree.ElementTree as ET
import glob
import csv

IDTransform = {'whisky':0,
               'vodka':1,
               'tequila':2}

def readXmlAnno(im_fn, ann_DIR):
    anno_pn = os.path.join(ann_DIR, im_fn + '.xml')
    # print 'On annotation: {}'.format(anno_pn)
    tree = ET.parse(anno_pn)
    root = tree.getroot()

    p_anno = {}
    size = root.find('size')
    d_size = {"width": size.find('width').text,
              "height": size.find('height').text,
              "depth": size.find('depth').text
              }
    p_anno['size'] = d_size

    l_obj = []
    for obj in root.findall('object'):
        d_obj = {"name": obj.find('name').text, "truncated": '0.0', "difficult": '0.0', "occluded": '0.0',
                 "xmin": float(obj.find('bndbox').find('xmin').text),
                 "ymin": float(obj.find('bndbox').find('ymin').text),
                 "xmax": float(obj.find('bndbox').find('xmax').text),
                 "ymax": float(obj.find('bndbox').find('ymax').text),
                 }
        l_obj.append(d_obj)

    p_anno['l_obj'] = l_obj

    if len(l_obj) > 0:
        return p_anno
    else:
        return None


if __name__ == '__main__':

    XmlfileDir = 'E:/bottleDataSet/Real/test/Annotations/'

    txtpath = 'E:/bottleDataSet/Real/Yolov3/Reallabel/'

    Grouptestpath = 'E:/bottleDataSet/Real/Yolov3/'

    # LabelFileList = []
    # xmlfiles = sorted(glob.glob(XmlfileDir + '*.xml'))
    # for im_fn  in xmlfiles:
    #     im_fn = os.path.basename(im_fn).split('.')[0]
    #     p_anno = readXmlAnno(im_fn, XmlfileDir)
    #
    #     annolist = p_anno['l_obj']
    #     txtData = []
    #     for it in annolist:
    #         tempdata = []
    #
    #
    #         x = (it['xmin'] + (it['xmax'] - it['xmin']) / 2) * 1.0 / 1280
    #
    #         y = (it['ymin'] + (it['ymax'] - it['ymin']) / 2) * 1.0 / 720
    #
    #         w = (it['xmax'] - it['xmin']) * 1.0 / 1280
    #
    #         h = (it['ymax'] - it['ymin']) * 1.0 / 720
    #
    #         tempdata.append(x)
    #         tempdata.append(y)
    #         tempdata.append(w)
    #         tempdata.append(h)
    #         tempdata.append(it['name'])
    #
    #
    #         txtData.append(tempdata)
    #
    #     file = open(txtpath + im_fn + '.txt', "w")
    #     LabelFileList.append(im_fn)
    #     for it in txtData:
    #         classid = it[4].lower()
    #         if classid in IDTransform:
    #             nameid = IDTransform[it[4].lower()]
    #         else:
    #             continue
    #         file.write(str(nameid) + ' ' + str(it[0]) + ' ' + str(it[1]) + ' ' + str(it[2]) + ' ' + str(it[3]) + '\n')
    #     file.close()
    #
    #
    #
    # LabelFileList = sorted(LabelFileList)

    file = open(Grouptestpath + 'RealtrainData.txt', "w")
    for it in range(8529):
        name = 'Real_' + str(it)
        temp = '/home/kobe/YoloV3_Pytorch/data/coco/images/realbottle/' + name + '.jpg'
        file.write(temp + '\n')
    file.close()






