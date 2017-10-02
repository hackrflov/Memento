1. 下载网易的repo文件
`wget http://mirrors.163.com/.help/CentOS6-Base-163.repo`

2. 备份系统原来的repo文件 
`mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak`

3. 替换系统的repo文件 
`mv CentOS6-Base-163.repo /etc/yum.repos.d/CentOS-Base.repo`

4. 执行yum源的更新命令
    ```bash
yum clean all
yum makecache
yum update
    ```

