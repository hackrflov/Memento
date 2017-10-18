有些时候对同样的网址(用myurl表示)，bash中
`$ curl myurl`
返回正常结果，但在python中却返回奇怪的内容
```python
import requests
r = requests.get(myurl)
```
这可能是因为发生了302重定向(redirection)，但curl阻止了重定向行为而requests模块默认没有，解决办法是在requests语句中加入参数
```python
import requests
r = requests.get(myurl, allow_redirects=False)
```
