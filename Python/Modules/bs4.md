Installation
------------
```bash
$ pip install beautifulsoup4 lxml
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
- soup.find_all(name, attrs, recursive, text, \*\*kwargs): use`recursive=False`to find direct children
- soup.find(name, attrs, recursive, text, \*\*kwargs)
- soup.select(tag + blank + attr)
- soup.get_text(separator)
