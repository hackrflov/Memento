### 详细介绍
[wikipedia](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
### 使用条件
目标数据含有分类标签  
### 方法
设定一个K，找出测试数据（unlabeled data)距离最近的K个点，根据这些点的类别归类
### 特色
简单易用
  
### 实现代码
```python
# use scikit-learn
from sklearn.neighbors import KNeighborsClassifier
k = 3  # set the parameter depending on your data
knn = KNeighborsClassifier(n_neighbors = k)
Y_pred = knn.predict(X_test)
acc_knn = knn.socre(X_test, Y_test)
```
