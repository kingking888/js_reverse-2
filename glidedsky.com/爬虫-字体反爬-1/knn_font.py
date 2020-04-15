# -*- encoding: utf-8 -*-
'''
@File    :   knn_font.py
@Time    :   2020/4/13 13:30:00
@Author  :   xahoo
@PythonVersion  :   3.6
@purpose ： （本文件是对测试文件knn_test.py的总结）
'''

import numpy as np
import pandas as pd
from font import get_font_data
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


class Classify(object):
    def __init__(self):
        self.len = None
        self.knn = self.get_knn()

    def process_data(self, data):
        # 处理缺失值,这里涉及到机器学习基本知识（新版本用 SimpleImputer）
        # 新旧版本区别：http://www.bubuko.com/infodetail-2926071.html
        # missing_values（缺失值），strategy(策略，默认平均值)，axis（选择行列，0为列，1为行）
        imputer = SimpleImputer(missing_values=np.nan, strategy='mean')  # # 缺省值选择空，策略为平均数，
        # 取出特征值，目标值
        return pd.DataFrame(imputer.fit_transform(pd.DataFrame(data)))

    def get_knn(self):
        # 取出特征值，目标值,传入data get_font_data()
        data = self.process_data(get_font_data())
        x_train = data.drop([0], axis=1)
        y_train = data[0]

        # 进行算法流程
        knn = KNeighborsClassifier(n_neighbors=1)
        # 开始训练
        knn.fit(x_train, y_train)

        self.len = x_train.shape[1]
        return knn

    # knn预测
    def knn_predict(self, data):
        df = pd.DataFrame(data)
        data = pd.concat(
            [df, pd.DataFrame(np.zeros((df.shape[0], self.len - df.shape[1])), columns=range(df.shape[1], self.len))])
        data = self.process_data(data)
        y_predict = self.knn.predict(data)
        return y_predict