import csv
from sklearn.svm import LinearSVC
import numpy as np
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib

class SVMManage(object):

    __train_feature_data = [] #特徴量
    __train_label_data = [] #特徴量

    __estimator = LinearSVC(C=1.0)     #SVM識別器

    #----------メンバ関数--------------
    #コンストラクタ
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    #特徴量ファイルを読み込む
    def ReadTrainFeatureFile(self,filename):
        with open(filename, 'r',encoding='cp932') as filename:
            reader = csv.reader(filename)
            #読み込む
            for row in reader:
                self.__train_feature_data.append(row)
        return

    #ラベルファイルを読み込む
    def ReadTrainLabelFile(self,filename):
        with open(filename, 'r',encoding='cp932') as filename:
            reader = csv.reader(filename)
            #読み込む
            for row in reader:
                self.__train_label_data.append(row[0])  #１次元のlistにするため
        return 

    def ExecTrain(self):
        #ndarray型に直さないと読んでくれないみたい
        n_feature_data = np.array(self.__train_feature_data)
        n_label_data = np.array(self.__train_label_data)        #ラベルデータは１次元にする

        #size_feaqture = len(self.__train_feature_data)
        #size_label = len(self.__train_label_data)

        # 学習
        self.__estimator.fit(n_feature_data,n_label_data)

        # 予測モデルをシリアライズ 作成した分類モデルを出力する
        joblib.dump(self.__estimator, 'estimator.pkl') 

        return
