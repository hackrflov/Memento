```python
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    return redirect(url)

# To get params
searchword = request.args.get('key', '')

# To allow cors
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
```

**注意：如果修改了本文件及关联的文件，则需要关闭重新打开**
