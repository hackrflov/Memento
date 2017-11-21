```python
from pymongo import MongoClient
client = MongoClient('mongodb://{0}:{1}@{2}:{3}'.format(usr, pwd, host, port))
db = client.db_name
```
+ db.clt.update_one(filter, { '$set' : { key : value } }, upsert=True)
+ db.clt.update_one(filter, { '$setToArray': { key : { '$each' : value } } }, upsert=True)
+ db.clt.delete_one(filter)
+ db.clt.delete_many(filter)

How to use Bulk-Write
---------------------
```python
from pymongo import UpdateOne
op = UpdateOne(filter, { '$set' : { key : value } }, upsert=True)
reqs.append(op)
db.clt.bulk_write(reqs)
