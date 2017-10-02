### 详细介绍
[wikipedia](https://en.wikipedia.org/wiki/Decision_tree_learning)  
### 方法
建立含有一系列节点的决策树，在每个节点数据被划分(split)为若干部分，通过特征(feature)做出进入下一个节点的决策(decision)。这样一来每个待判定的数据将依次经过节点最终到达唯一的归类。建立最佳决策树的方法是用母节点的熵(Entropy)减去加权后的子节点熵(Weighted Sum of Entropy)从而计算每个特征的信息增益（Information gain），以此排序依次构建节点。  
### 特色
可以同时处理数值型和标签型数据，不需要对数据做特殊处理，能够处理大量数据；准确度不够高，容易过度拟合(overfit)  
  
### 实现代码
```python
# use scikit-learn
from sklearn.tree import DecisionTreeClassifier  
decision_tree = DecisionTreeClassifier()  
decision_tree.fit(X_train, Y_train)  
Y_pred = decision_tree.predict(X_test)  
acc_decision_tree = decision_tree.score(X_test, Y_test)  
```
