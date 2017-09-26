如何建立并使用子域名:
Step1. 设置DNS 
在购买域名的平台上设置DNS，添加CNAME类型，【主机】填子域名（例如api、blog），【指向】填@即可，TTL设置为1小时。（注意不要设置成A类型，会导致冲突）
Step2. 设置主机映射
在Apache的设置文件末尾(CentOS的path为/etc/httpd/conf/httpd.conf)，添加以下内容：
RewriteEngine on
RewriteCond %{HTTP_HOST} !^www.host.com [NC]
RewriteRule ^(.\*)$ %{HTTP_HOST}$1
RewriteRule  ^(.\*)\.host\.com(.\*)$ /$1$2 [L]
Step3. 设置相应文件夹
在/var/www/html目录下建立对应子域名的文件夹，即可正常使用。
