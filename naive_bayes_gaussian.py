# coding=utf-8
from sklearn.naive_bayes import GaussianNB

#0:晴 1:阴 2:降水 3:多云
data_table = [["date", "weather"],
              [1, 0],
              [2, 1],
              [3, 2],
              [4, 1],
              [5, 2],
              [6, 0],
              [7, 0],
              [8, 3],
              [9, 1],
              [10, 1]]
#当天的天气
X = [[0], [1], [2], [1], [2], [0], [0], [3], [1]]

#当天的天气对应后一天的天气
Y = [1, 2, 1, 2, 0, 0, 3, 1, 1]

# X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# Y = np.array([1, 1, 1, 2, 2, 2])
#现在我们把训练数据，和对应的分类放入分类器中进行训练
clf = GaussianNB().fit(X, Y)

#预测当天是晴天后一天的天气
p = [[1]]
print clf.predict(p)


#疾病预测
#基因片段A  基因片段B 高血压 胆结石
#1: 是    0：否
data_table = [
    [1, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]

#基因片段
X = [[1, 1], [0, 0], [0, 1], [1, 0], [1, 1], [1, 0], [0, 1], [0, 0], [1, 0], [0, 1]]

#高血压
y1 = [1, 0, 0, 0, 0, 0, 1, 0, 1, 0]

#训练
clf = GaussianNB().fit(X, y1)

#预测
p = [[1, 0]]
print clf.predict(p)

#胆结石
y2 = [0, 1, 0, 0, 1, 1, 1, 0, 0, 1]

#训练
clf = GaussianNB().fit(X, y2)

#预测
p = [[1, 0]]
print clf.predict(p)
