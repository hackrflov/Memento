详细介绍：https://en.wikipedia.org/wiki/Stochastic_gradient_descent
方法：通过迭代使Loss Function最小化

==== Scikit-Learn ====
from sklearn.linear_model import SGDClassifier
sgd = SGDClassifier()
sgd.fit(X_train, Y_train)
Y_pred = sgd.predict(X_test)
acc_sgd = sgd.score(X_test, Y_test)
