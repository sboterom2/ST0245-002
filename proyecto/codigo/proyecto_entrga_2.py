from matplotlib import pyplot as plt
import numpy as np
import csv

data= np.loadtxt('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/datasets/csv/enfermo_csv/00000004_66324407_ver1.csv', skiprows=0, delimiter=',')

def comp(m, dst_h, dst_w):
    ori_h, ori_width = m.shape
    ratio_h = ori_h / dst_h
    ratio_w = ori_width / dst_w
    dst = np.zeros((dst_h, dst_w), np.uint8)
    for h in range(dst_h):
        for w in range(dst_w):
            x_ori = int(w * ratio_w)
            y_ori = int(h * ratio_h)          
            dst[h, w] = m[y_ori, x_ori]       
    return dst    


img= comp(data,150,150)    

imgplot = plt.imshow(img, cmap = "gray")
plt.show

np.savetxt("foo.csv", img, delimiter=",")