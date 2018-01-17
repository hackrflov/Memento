
```python
from gevent import monkey
monkey.patch_all()

pool = ThreadPool(10)
pool.map(my_func, my_arrays)  # type is str
```
