详细介绍：https://en.wikipedia.org/wiki/Logistic_regression
使用条件：目标数据满足伯努利分布（0 or 1）
方法：套用Logistic Function，学习得出最接近实际的参数L,k,x0
特点：简单易用、首选方法

==== Scikit-Learn ====
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
Y_pred = logreg.predict(X_test)
acc_log = logreg.score(X_test, Y_test)

