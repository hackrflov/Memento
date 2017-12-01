注意[a for a in list]这个语句可能会修改外部变量，所以取名要谨慎
```python
>>> a = { 'a' : 2 }
>>> t = [a for a in [{'b': 1}]]
>>> print a
>>> { 'b' : 1 }
```
