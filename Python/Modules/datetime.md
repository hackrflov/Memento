```python
from datetime import datetime
# 将dt转化为时间戳
import calendar
calendar.timegm(dt.timetuple())
import time
time.mktime(dt.timetuple())
```
- `datetime.strptime(dtstr, format)`: 将日期字符串转化为dt变量 
- `datetime.fromtimestamp(ts)`: 将时间戳转化为dt变量
- `datetime.utcfromtimestamp(ts)`: 将时间戳转化为标准时区dt变量

- `timedelta.total_seconds()`: 将间隔转化为时间
