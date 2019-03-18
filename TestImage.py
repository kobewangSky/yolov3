import cv2
import glob
import os


_labelDir = os.path.join(os.getcwd(), 'data/coco/labels/trainbottle')
_ImageDir = os.path.join(os.getcwd(), 'data/coco/images/trainbottle')
_testDir = os.path.join(os.getcwd(), 'Testimage')

temp = os.path.exists(_labelDir)

Imagepaths = sorted(glob.glob(os.path.join(_ImageDir, '*.png')))

for it in Imagepaths:
    label_file = it.replace('images', 'labels').replace('.png', '.txt').replace('.jpg', '.txt')
    image = cv2.imread(it)
    img_h, img_w, img_c = image.shape
    image = image.copy()

    if os.path.exists(label_file) is not True:
        continue

    text_file = open(label_file, 'r')
    lines = text_file.readlines()
    for txtline in lines:
        temp = txtline.split(' ')
        x = float(temp[1])
        y = float(temp[2])
        w = float(temp[3])
        h = float(temp[4])

        xmin = x * img_w - ((w * img_w) / 2)
        ymin = y * img_h - ((h * img_h) / 2)

        xmax = xmin + (w * img_w)
        ymax = ymin + (h * img_h)

        cv2.circle(image, (int(xmin), int(ymin)), 2, (0, 255, 0) , -1)
        cv2.circle(image, (int(xmax), int(ymax)), 2, (0, 255, 0), -1)

    imagename = os.path.basename(it)
    temp = os.path.join(_testDir, imagename)
    cv2.imwrite(temp, image)


    print('')





