```python
import requests
res = requests.post(url, auth=('usr', 'pwd'))

# MIME: {file_field: (name, content, content_type, additional_file_headers)}
res = requests.post('http://test.com/upload', files={'data': ('readme.txt', 'Readme file content or pointer', 'text/plain')})
```
