```python
import pdb
pdb.set_trace()
```
How to use in shell
-------------------
```bash
$ python your_file.py
(Pdb) current line
```

## Common Operations
- n(next): next line
- s(step): can break out of loop
- d(down): move stack trace level down (useful when error occurs)
- c(continue): continue until breakpoint
- l(list): list current code
- a(args): print argument list
- unt(il): continue until certain line
