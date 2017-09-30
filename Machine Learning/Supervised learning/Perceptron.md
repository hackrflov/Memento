详细介绍：https://en.wikipedia.org/wiki/Perceptron
使用条件：目标数据含有二元标签
方法：设定一组参数w，初始值可全为0，与input x做点积得到y(t)，根据y(t)与实际d的差值更新w，重复此流程直到误差小于规定值
特点：支持在线学习(online learning)

==== Scikit-Learn ====
from sklearn.linear_model import Perceptron
perceptron = Perceptron()
perceptron.fit(X_train, Y_train)
Y_pred = perceptron.predict(X_test)
acc_perceptron = perceptron.score(X_test, Y_test)
