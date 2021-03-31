在create-react-app项目根目录，新建文件.env.production
写入这一句
GENERATE_SOURCEMAP=false
（为了隐藏源码）

然后在public里新建.htaccess
写入
Options -MultiViews
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^ index.html [QSA,L]
（为了支持router）

npm run build会生成build文件夹，这里面已经不包含map，所以隐藏了源码

接下来转移到服务器目录中
rm -r /var/www/html; cp  -rTf ~/your-project/build /var/www/html


在DNS服务商设置子域名
CNAME yoursubdomain-name hostname

编辑/etc/apache2/apache2.conf
<VirtualHost *:80>
    ServerName subdomain.domain.art
    ProxyPass / http://localhost:port/
    ProxyPassReverse / http://localhost:port/
</VirtualHost>

