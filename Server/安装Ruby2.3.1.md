# 安装开发工具集
yum groupinstall "Development Tools"  

# 下载并安装
cd /tmp
wget https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.xz
tar xpvf ruby-2.3.1.tar.xz
./configure  
make  
make install

# 查看版本
ruby -v  


