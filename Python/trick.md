# 深度遍历嵌套dict & list，将unicode编码为utf-8格式str
```python
def encode(self, doc):
    if type(doc) == dict:
        for k, v in doc.items():
            if type(v) == dict:
                self.encode(v)
            elif type(v) == list:
                for i in v:
                    self.encode(i)
            elif type(v) == unicode:
                doc[k] = v.encode('utf-8')
```
