import cv2
import os
from tqdm import tqdm

def pic_list(path):
    PicList = os.listdir(path)
    M = len(PicList)
    for i in tqdm(range(M)):
        PicList[i] = path + PicList[i]
        img = crop_img(PicList[i])
        cv2.imwrite(path+"/crop/"+str(i+1)+".jpg",img)
        pass


def crop_img(path):
    img = cv2.imread(path)
    img = img[100:980,400:1780]
    return img


if __name__ == '__main__':
    #path = "/home/zhangcheng/data/1/"
    path = input("please input your dir path:")
    PicList = pic_list(path)
