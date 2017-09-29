# 使用rubychina的镜像源
$ gem sources --add https://gems.ruby-china.org/ --remove https://rubygems.org/

# 确保只有 gems.ruby-china.org
$ gem sources -l
https://gems.ruby-china.org

# 加快bundle
$ bundle config mirror.https://rubygems.org https://gems.ruby-china.org
