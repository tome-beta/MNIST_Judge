# -*- coding: utf-8 -*-
import numpy as np
import csv
import cv2

def open_with_python_csv(filename):
    data = []
    with open(filename, 'r',encoding='cp932') as filename:
        reader = csv.reader(filename)
        #中身
        for row in reader:
            data.append(row)
    return data
    
# %%
if __name__ == '__main__': #main関数
    #csvファイルを読み込む
    csv_name = 'D:/myprog/MNIST_Judge/data/test.csv'
    name_list = open_with_python_csv(csv_name)

    print(name_list[0])
    
    #画像の読み込み
#    img = cv2.imread('D:/myprog/MNIST_Judge/data/train-images-idx3-ubyte/t10k-images-idx3-ubyte/img/img00001.png',0)
    img = cv2.imread(name_list[0][0],0) #２次元配列になっている
    
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
 

    end = 100
    
