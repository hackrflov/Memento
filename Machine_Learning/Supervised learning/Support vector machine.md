### 详细介绍
[wikipedia](https://en.wikipedia.org/wiki/Support_vector_machine)
### 使用条件
目标数据可以被归类为两类中的一类
### 方法
构造一个超平面将所有数据划分为两类，使得该超平面离两边最近点的距离之和最大
### 特色
准确度高、灵活
### 知识点
- Linear SVM:
    - Hard-Margin: [Linearly seperable] All points fall out of the margin
    - Soft-Margin: [Not linearly seperable] Some points fall in the margin
- Nonlinear classification

  
### 实现代码
```python
# use scikit-learn
from sklearn.svm import SVC, LinearSVC
svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
acc_svc = svc.score(X_test, Y_test)

linear_svc = LinearSVC()
linear_svc.fit(X_train, Y_train)
Y_pred = linear_svc.predict(X_test)
acc_linear_svc = linear_svc.score(X_test, Y_test)
```
