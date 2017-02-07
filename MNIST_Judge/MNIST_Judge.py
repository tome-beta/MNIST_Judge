# -*- coding: utf-8 -*-
import numpy as np
import csv
import cv2
import matplotlib
import matplotlib.pyplot as plt
    

class MNIST_Data(object):
    #定数
    IMG_WIDTH = 28
    IMG_HEIGTH = 28

    #メンバ変数
    __file_name_list = [] #ファイル名リスト　文字列
    __file_label_list = [] #ラベルリスト

    __pix_data = [] #

    #----------メンバ関数--------------
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

    #画像を２値化してListとして返す
    def convertThreshold(self,gray_img):
        pixel_data = []

        #２値化を行う
        _,threshold_img = cv2.threshold(gray_img, 60, 255, cv2.THRESH_BINARY)
        threshold_img = cv2.cvtColor(threshold_img, cv2.COLOR_GRAY2RGB)

        #28*28の画像
        pixel_data = []
        for y in range(self.IMG_HEIGTH):
            for x in range(self.IMG_WIDTH):
                pixel = threshold_img[y,x]
                #２値化した画素を０か１で表す
                if pixel[0] == 0 :
                    pixel_data.append(0)
                else :
                    pixel_data.append(1)
        return pixel_data

    def TransFormImgData(self):
        no = 0
        while no < len(self.__file_label_list) :
            #画像を読み込む
            gray_img = cv2.imread(train_data.GetFileName(no),0) 

            #画層を２値化して０か１の値のListとして返す
            pixel_data = self.convertThreshold(gray_img)

            #list[list[]]の形になる
            self.__pix_data.append(pixel_data)
            no += 1

        return 

    #手書き文字を２値化した特徴量をファイルに書き出す
    def OutPutTrainData(self):
        output_name = "train_feature.csv"
        with open(output_name,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.__pix_data)
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
    csv_name = 'D:/myprog/MNIST_Judge/data/train_image.csv'
    label_name = 'D:/myprog/MNIST_Judge/data/train_label.csv'
#    csv_name = 'D:/myprog/MNIST_Judge/data/train_image_test.csv'
#    label_name = 'D:/myprog/MNIST_Judge/data/train_label_test.csv'

    #クラスのインスタンス化
    train_data = MNIST_Data()
    train_data.OpenFileNameCSV(csv_name)
    train_data.OpenLabelCSV(label_name)
    train_data.TransFormImgData()
    train_data.OutPutTrainData()


    print(train_data.GetFileName(0))
    
    #画像を読み込む
#    img = cv2.imread('D:/myprog/MNIST_Judge/data/train-images-idx3-ubyte/t10k-images-idx3-ubyte/img/img00001.png',0)
    img = cv2.imread(train_data.GetFileName(0),0) 
    
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
 

    end = 100
    
