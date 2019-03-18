import os
import glob

import json
import shutil
import cv2


# IDTransform = {'bottles_Bottle_s_Jack_Daniels_Object0011':'whisky',
#                'Bottle_s_Absolut_vodka_Bottle_s_Absolut_vodka_Line001':'vodka',
#                'Bottle_s_Bombay_sapphire_Bottle_s_Bombay_sapphire_Box0012' : 'sapphire',
#                'Bottle_s_Cachaca_Bottle_s_Cachaca_Line001_2':'cachaca',
#                'Bottle_s_Cachaca_nega_Bottle_s_Cachaca_nega_Line003_1':'nega',
#                'Bottle_s_Campari_Bottle_s_Campari_Object008':'campari',
#                'Bottle_s_Gordon_Gin_Bottle_s_Gordon_Gin_Object0018' : 'gin',
#                'Bottle_s_Havana_Club_Bottle_s_Havana_Club_Object011':'havana',
#                'Bottle_s_J_B_Bottle_s_J_B_Line005':'j_b',
#                'Bottle_s_Jose_Cuervo_Bottle_s_Jose_Cuervo_Object0027':'tequila',
#                'Bottle_s_Martini_Bianco_Bottle_s_Martini_Bianco_Line0017':'bianco',
#                'Bottle_s_Sambuca_Bottle_s_Sambuca_Line0022':'sambuca',
#                'Bottle_s_Sauza_Bottle_s_Sauza_Box0013':'sauza',
#                'Bottle_s_Martini_Rosso_Bottle_s_Martini_Rosso_Line0011':'Rosso'}

IDTransform = {'bottles_Bottle_s_Jack_Daniels_Object0011':0,
               'Bottle_s_Absolut_vodka_Bottle_s_Absolut_vodka_Line001':1,
               'Bottle_s_Jose_Cuervo_Bottle_s_Jose_Cuervo_Object0027':2}


_testDir = os.path.join(os.getcwd(), 'Testimage')

def removecoverdata(boundingboxlist, ymin, xmin, ymax, xmax, lower):

    needremove = []
    Covered = False
    for it in boundingboxlist:
        if it['xmin'] < xmin and it['ymin'] < ymin and it['xmax'] > xmax and it['ymax'] > ymax:
            Covered = True
            break
        if it['xmin'] > xmin and it['ymin'] > ymin and it['xmax'] < xmax and it['ymax'] < ymax:
            needremove.append(it)
            continue

    if Covered == False:
        boundingboxlist.append({'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax, 'class': lower})

    for it in needremove:
        boundingboxlist.remove(it)

    return boundingboxlist

clamp = lambda n, minn, maxn :max(min(maxn, n), minn)

if __name__ == '__main__':

    RawDir = './data/coco/VirtualRaw'

    ImageTargetDir = './data/coco/images/trainbottle'

    LabelTargetDir = './data/coco/labels/trainbottle'

    # listdir = os.listdir(RawDir)
    #
    # FileNameIndex = 0
    #
    # for listdir_temp in listdir:
    #     TempDir = os.path.join(RawDir, listdir_temp)
    #
    #     if os.path.isdir(TempDir) != True:
    #         continue
    #
    #     #Imagegroup = sorted(glob.glob(os.path.join(ImageTargetDir, '*.png')))
    #     #Imagegroup = sorted(Imagegroup, key=lambda f: int(os.path.basename(f).split('.')[0]))
    #
    #     Imagegroup = sorted(glob.glob(os.path.join(TempDir, '??????.png')))
    #     Jsongroup = sorted(glob.glob(os.path.join(TempDir, '??????.json')))
    #
    #     if len(Imagegroup) != len(Jsongroup):
    #         assert 'Data Fail'
    #         break
    #
    #     FileNameIndextemp = FileNameIndex
    #
    #     # print("Start Image Copy")
    #     # for Filepath in Imagegroup:
    #     #     TargetPathTemp = os.path.join(ImageTargetDir, str(FileNameIndextemp)) + '.png'
    #     #     shutil.copy2(Filepath, TargetPathTemp)
    #     #     FileNameIndextemp = FileNameIndextemp + 1
    #     #     print(FileNameIndextemp)
    #     # print("End Image Copy")
    #
    #     FileNameIndextemp = FileNameIndex
    #
    #     TrainLabelList = []
    #
    #     for i in range(len(Jsongroup)):
    #         jsonFilepath = Jsongroup[i]
    #         json_file = open(jsonFilepath)
    #         Data = json.load(json_file)
    #
    #         img = cv2.imread(Imagegroup[i])
    #         # img = img.copy()
    #
    #         img_h, img_w, img_c = img.shape
    #         boundingboxlist = []
    #
    #         for p in Data['objects']:
    #
    #             strname = p['class']
    #
    #             ymin = p['bounding_box']["top_left"][0]
    #             ymin = int(clamp(ymin, 0, img_h))
    #
    #             xmin = p['bounding_box']["top_left"][1]
    #             xmin = int(clamp(xmin, 0, img_w))
    #
    #             ymax = p['bounding_box']["bottom_right"][0]
    #             ymax = int(clamp(ymax, 0, img_h))
    #
    #             xmax = p['bounding_box']["bottom_right"][1]
    #             xmax = int(clamp(xmax, 0, img_w))
    #
    #             if ymin == ymax or xmin == xmax:
    #                 continue
    #
    #             if strname in IDTransform :
    #                 lower = IDTransform[strname]
    #             else:
    #                 continue
    #
    #
    #
    #             boundingboxlist = removecoverdata(boundingboxlist, ymin, xmin, ymax, xmax, lower)
    #
    #         output = []
    #         for it in boundingboxlist:
    #             xmin = it['xmin']
    #             ymin = it['ymin']
    #             xmax = it['xmax']
    #             ymax = it['ymax']
    #             id = it['class']
    #
    #             x = (xmin + (xmax - xmin) / 2) * 1.0 / img_w
    #
    #             y = (ymin + (ymax - ymin) / 2) * 1.0 / img_h
    #
    #             w = (xmax - xmin) * 1.0 / img_w
    #
    #             h = (ymax - ymin) * 1.0 / img_h
    #
    #             output.append({'xmin': x, 'ymin': y, 'xmax': w, 'ymax': h, 'class': id})
    #
    #
    #
    #             # cv2.circle(img, (xmin, ymin), 2, (0, 255, 0), -1)
    #             # cv2.circle(img, (xmax, ymax), 2, (0, 255, 0), -1)
    #
    #         # imagename = os.path.basename(Imagegroup[i])
    #         # temp = os.path.join(_testDir, imagename)
    #         # cv2.imwrite(temp, img)
    #
    #
    #
    #         NameTemp = str(FileNameIndextemp)
    #
    #         file = open(os.path.join(LabelTargetDir, NameTemp) + '.txt', "w")
    #         for it in output:
    #             file.write(f'{it["class"]} {it["xmin"]} {it["ymin"]} {it["xmax"]} {it["ymax"]} \n')
    #         file.close()
    #         FileNameIndextemp = FileNameIndextemp + 1
    #         TrainLabelList.append(file)
    #         print(FileNameIndextemp)
    #
    #     print("Finish ImageSets")

    file = open(os.path.join(os.getcwd() + '/data/coco/', 'trainbottle') + '.txt', "w")
    for i in range(60000):
        temp = os.getcwd() + '/data/coco/images/trainbottle/'
        temp = temp + str(i) + '.png'
        file.write(temp + '\n')
    file.close()