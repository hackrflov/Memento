```python
## WRITE
f = open(file_path, 'w')
f.write('Your File String')
# f.truncate() # if you need cover old content, uncomment this
f.close()

## READ
f = open(file_path, 'r')
text = f.read()
```
