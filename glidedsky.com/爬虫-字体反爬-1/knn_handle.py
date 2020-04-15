# -*- encoding: utf-8 -*-
'''
@File    :   knn_test.py
@Time    :   2020/4/13 11:00:00
@Author  :   xahoo
@PythonVersion  :   3.6
@purpose ：  所有字体获取所有字体所被代表的  数字+坐标(放在列表)已经全部获取到，现在我们来测试一下准确率(使用knn算法训练数据)
'''
import numpy as np
import pandas as pd
from font import get_font_data
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def main():
    import pprint
    x=get_font_data()
    # pprint.pprint(x)
    # 处理缺失值,这里涉及到机器学习基本知识（新版本用 SimpleImputer）
    # 新旧版本区别：http://www.bubuko.com/infodetail-2926071.html
    # missing_values（缺失值），strategy(策略，默认平均值)，axis（选择行列，0为列，1为行）
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')  # # 缺省值选择空，策略为平均数，

    # 取出特征值，目标值
    data = pd.DataFrame(imputer.fit_transform(pd.DataFrame(x)))
    x = data.drop([0], axis=1)
    y = data[0]

    # 分割数据集
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0) （随机分割方式）
    # 由于采集的字体数据不多，如果按随机分割的方式，训练集容易缺失某些字符，导致预测测试集的结果误差率较大，
    # 所以在此固定前40个样本为训练集，最后10个样本为测试集合。
    x_train = x.head(40)
    y_train = y.head(40)
    x_test = x.tail(10)
    y_test = y.tail(10)

    # 标准化
    # 多次测试发现，此处进行标准化，会影响成功率，所以不采用，另外k值取1, 也就是说，我判定当前样本跟离它最近的那个样本属于同一类型，
    # 即同一个字符，这个值取多少合适经过调试才知道，最后预测10个样本，包含了0-9 10个字符，成功率为100%。
    # std = StandardScaler()
    # x_train = std.fit_transform(x_train)
    # x_test = std.transform(x_test)

    # 进行算法流程
    knn = KNeighborsClassifier(n_neighbors=1)

    # 开始训练
    knn.fit(x_train, y_train)

    # 预测结果
    y_predict = knn.predict(x_test)
    print("1y", y)
    print("2y", y_predict)

    # 得出准确率
    print(knn.score(x_test, y_test))


main()