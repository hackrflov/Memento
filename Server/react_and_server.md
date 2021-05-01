在create-react-app项目根目录，新建文件.env.production
写入这一句
GENERATE_SOURCEMAP=false
（为了隐藏源码）

npm run build会生成build文件夹，这里面已经不包含map，所以隐藏了源码


为了支持react-router
1.a2enmod rewrite
2.Open up /etc/apache2/apache2.conf
3.Paste in this with the path to your root:
<Directory "/var/www/PATH_TO_YOUR_ROOT">
    RewriteEngine on
    # Don't rewrite files or directories
    RewriteCond %{REQUEST_FILENAME} -f [OR]
    RewriteCond %{REQUEST_FILENAME} -d
    RewriteRule ^ - [L]
    # Rewrite everything else to index.html to allow html5 state links
    RewriteRule ^ index.html [L]
</Directory>
4.sudo service apache2 restart

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

