### 详细介绍
[wikipedia](https://en.wikipedia.org/wiki/Logistic_regression)
### 使用条件
目标数据满足伯努利分布（0 or 1）
### 方法
套用Logistic Function，学习得出最接近实际的参数L,k,x0
### 特色
简单易用、首选方法
  
### 实现代码
```python
# use scikit-learn
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
Y_pred = logreg.predict(X_test)
acc_log = logreg.score(X_test, Y_test)
```
