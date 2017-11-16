如果在Linux平台中用yum update指令返回如下内容，则说明python包不匹配。  

There was a problem importing one of the Python modules
required to run yum. The error leading to this problem was:

No module named yum

Please install a package which provides this module, or
verify that the module is installed correctly.

It's possible that the above module doesn't match the
current version of Python, which is:
2.7.13 (default, Aug 14 2017, 18:10:49) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-18)]

If you cannot solve this problem yourself, please go to 
the yum faq at:
 http://yum.baseurl.org/wiki/Faq

解决办法
--------
```bash
# 要从库中找到装有yum包的python版本
find / -type f -executable -name 'python2*'
# 输出如下
/usr/bin/python2.6
/usr/bin/python2.7
...
# 对于每条路径，直接运行
/usr/bin/python2.x
# 进入python程序，尝试导入yum包
>>> import yum
# 不断尝试直到碰上可以成功导入的python版本
vim /usr/bin/yum
# 修改yum文件，将第一行改为新版本即可
#!/usr/bin/python2.7
```
