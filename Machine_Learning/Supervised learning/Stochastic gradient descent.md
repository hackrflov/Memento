### 详细介绍
[wikipedia](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)
### 使用条件
目标数据含有分类标签  
### 方法
通过迭代使Loss Function最小化
  
### 实现代码
```python
# use scikit-learn
from sklearn.linear_model import SGDClassifier
sgd = SGDClassifier()
sgd.fit(X_train, Y_train)
Y_pred = sgd.predict(X_test)
acc_sgd = sgd.score(X_test, Y_test)
```
