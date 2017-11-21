### 详细介绍
[wikipedia](https://en.wikipedia.org/wiki/Random_forest)
### 使用条件
目标数据含有分类标签  
### 方法
用改良的Tree bagging方法生成B个不同的样本与相对应的决策树（改良的标准是用随机特征子集(random subset of the features)而非全部特征），然后对于每个待预测的数据，遍历B个决策树，对产生的B个结果取平均数或取频次最大的结果。
### 特色
消除了单一决策树过度拟合的问题，准确度很高
  
### 实现代码
```python
# use scikit-learn
from sklearn.ensemble import RandomForestClassifier
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, Y_train)
Y_pred = random_forest.predict(X_test)
acc_random_forest = random_forest.score(X_test, Y_test)
```
