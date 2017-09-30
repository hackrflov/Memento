详细介绍：https://en.wikipedia.org/wiki/Naive_Bayes_classifier
使用条件：目标数据含有类别标签，各个影响因素互不关联（independent)
方法：用高斯分布等模型计算出条件概率（类别为C时factor为F的概率-> p(f=F|C)，
      则类别为C1的概率为p(C1|f1,f2...fn)=p(C)p(f1|C)p(f2|C)...p(fn|C)/evidence，
      只需要比较p(Ci|f1,f2...fn)之间的大小即可,Ci属于所有类别中的一种
应用场景：垃圾邮件识别（Spam Email)

==== Scikit-Learn ====
from sklearn.naive_bayes import GaussianNB
gaussian = GaussianNB()
gaussian.fit(X_train, Y_train)
Y_pred = gaussian.predict(X_test)
acc_gaussian = gaussian.score(X_test, Y_test)
