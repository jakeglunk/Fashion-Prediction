import cv2
import os

folderpath='/home/jake/Downloads/Segmentation/Boots_img'
images = os.listdir(folderpath)

for file in images:
    print(file)

    img = cv2.imread(str('Boots_img/'+file))

    base_w = img.shape[1]
    base_h = img.shape[0]

    h_scale = 800/base_h
    w_scale = 600/base_w

    x_spacer = 0
    y_spacer = 0
    x_spacer1 = 0
    y_spacer1 = 0

    if base_w >= base_h:
        scale = 600/base_w

    if base_h > base_w:
        scale = 800/base_h

    width = int(base_w*scale)
    height = int(base_h*scale)

    if width >600:
        diff = int(width-600)
        width = int(width-diff)
        height = int(height-diff)

    if width < 600:
        x_spacer = (600 - width)/2
        x_spacer1 = x_spacer
        if x_spacer %2 != 0:
            x_spacer= int(x_spacer)
            x_spacer1 = int(x_spacer1+1)
        x_spacer = int(x_spacer)
        x_spacer1 = int(x_spacer1)


    if height < 800:
        y_spacer = (800- height)/2
        y_spacer1 = y_spacer
        if y_spacer %2 != 0:
            y_spacer=int(y_spacer)
            y_spacer1 = int(y_spacer1+1)
        y_spacer = int(y_spacer)
        y_spacer1 = int(y_spacer1)

    if int(width+x_spacer+x_spacer1) >600:
        width = width-1

    dim = (width,height)
    print(dim,(x_spacer,x_spacer1),(y_spacer,y_spacer1))

    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    bordered = cv2.copyMakeBorder(resized, y_spacer, y_spacer1, x_spacer, x_spacer1, cv2.BORDER_CONSTANT, value=([255,255,255]))

    print(bordered.shape)

    cv2.imwrite("{}".format(file),bordered)
