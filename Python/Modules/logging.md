```python
import logging
logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S")
log = logging.getLogger('myLoggerName')

# To print full trace stack
try:
    # do your work
except Exception as e:
    log.exception(e)
```
