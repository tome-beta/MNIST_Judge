import csv
from sklearn.svm import LinearSVC
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib

from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn import svm

class SVMManage(object):

    __train_feature_data = [] #特徴量
    __train_label_data = [] #特徴量

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

    #読み込んだ学習データより学習を行う　モデルを出力
    def ExecTrain(self):
        #ndarray型に直さないと読んでくれないみたい
        n_feature_data = np.array(self.__train_feature_data,np.float64)
        n_label_data = np.array(self.__train_label_data,np.float64)        #ラベルデータは１次元にする

        #size_feaqture = len(self.__train_feature_data)
        #size_label = len(self.__train_label_data)

        # 学習
        estimator = LinearSVC(C=1.0)     #SVM識別器
        estimator.fit(n_feature_data,n_label_data)

        # 予測モデルをシリアライズ 作成した分類モデルを出力する
        joblib.dump(estimator, 'estimator.pkl') 

        return

    #学習モデルを読み込んで、テスト実行
    def ExecPredict(self):

        digits = load_digits()
        print(digits.data.shape)
        data_train, data_test, label_train, label_test = train_test_split(digits.data, digits.target)
        lin_svc = svm.LinearSVC()
        lin_svc.fit(data_train, label_train)
        lin_svc.predict(data_test)
        # 予測モデルをロード
        svm_org = LinearSVC()
        svm_model = joblib.load('estimator.pkl')

        #ここで判定したい
        n_feature_data = np.array(self.__train_feature_data,np.float64)
        n_label_data = np.array(self.__train_label_data)        #ラベルデータは１次元にする
        result = svm_model.predict(n_feature_data)

        #ndarrayをcsvファイルに出力
        np.savetxt("result.csv", result, fmt="%d",delimiter=",")
        return