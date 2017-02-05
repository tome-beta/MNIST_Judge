# -*- coding: utf-8 -*-
import numpy as np
import csv
import cv2

    

class MNIST_Data(object):
    #メンバ変数
#    name_list
    #----------メンバ関数--------------
    __file_name_list = [] #ファイル名リスト　文字列
    __file_label_list = [] #ラベルリスト

    #コンストラクタ
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    #ファイル名リストを渡してファイル名を読み込む
    def OpenFileNameCSV(self,filename):
        with open(filename, 'r',encoding='cp932') as filename:
            reader = csv.reader(filename)
            #読み込む
            for row in reader:
                self.__file_name_list.append(row)
        return 

    #ラベルをCSVから読み込む
    def OpenLabelCSV(self,filename):
        with open(filename, 'r') as filename:
            reader = csv.reader(filename)
            #読み込む
            for row in reader:
                self.__file_label_list.append(row)
        return 

    #ファイル名を取得
    def GetFileName(self,no):
        return self.__file_name_list[no][0]

    #ラベル名を取得
    def GetFileLabel(self,no):
        return self.__file_label_list[no][0]

# %%
if __name__ == '__main__': #main関数

    #csvファイルからファイル名を取得
    csv_name = 'D:/myprog/MNIST_Judge/data/t10k_train.csv'
    label_name = 'D:/myprog/MNIST_Judge/data/t10k_label.csv'

    #クラスのインスタンス化
    train_data = MNIST_Data()
    train_data.OpenFileNameCSV(csv_name)
    train_data.OpenLabelCSV(label_name)

    print(train_data.GetFileName(0))
    
    #画像を読み込む
#    img = cv2.imread('D:/myprog/MNIST_Judge/data/train-images-idx3-ubyte/t10k-images-idx3-ubyte/img/img00001.png',0)
    img = cv2.imread(train_data.GetFileName(0),0) 
    
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
 

    end = 100
    
