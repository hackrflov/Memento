# 如何在CentOS中安装中文字体
1. 首先拷贝字体包, Mac在/Library/Fonts中, Windows在C:\Windows\Fonts\, 将文件拷贝至Linux存放字体的文件夹中 /usr/share/fonts
2. 安装字体
```bash
$ mkdir /usr/share/fonts/chinese
$ cd /usr/share/fonts/chinese
$ yum install mkfontscale -y
$ yum install fontconfig
$ mkfontscale
$ mkfontdir
$ fc-cache -fv
$ source /etc/profile
# 输出检查
$ fc-list :lang=zh
```
