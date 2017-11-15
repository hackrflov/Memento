```python
from pymongo import MongoClient
client = MongoClient('mongodb://{0}:{1}@{2}:{3}'.format(usr, pwd, host, port))
db = client.db_name
```
+ db.clt.update_one(filter, { '$set' : { key : value } }, upsert=True)
+ db.clt.update_one(filter, { '$setToArray': { key : { '$each' : value } } }, upsert=True)
