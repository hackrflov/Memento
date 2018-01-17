```python
import grequests

urls = [
    'https://www.sogou.com/web?query=a',
    'https://www.sogou.com/web?query=b',
    'https://www.sogou.com/web?query=c',
    'https://www.sogou.com/web?query=d',
]

# 最先执行这个函数，然后才是整个requests
def hook(r, **kwargs):
    print r.url, r.text[:10]
    return r

rs = [grequests.get(u, hooks={'response': hook}) for u in urls]
requests = grequests.map(rs)
```
