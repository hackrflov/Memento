Installation
------------
```bash
$ pip install beautifulsoup4
```
Usage
-----
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
```

Methods
-------
- soup.tagname[classname]
- soup.tagname.get(classname)
- soup.find_all(name, attrs, recursive, text, \*\*kwargs)
- soup.find(name, attrs, recursive, text, \*\*kwargs)
- soup.select(tag + blank + attr)
