注意以下语句
```python
for item in my_list: 
    item = another_item
```
如果是将另一个值赋予列表元素，并不会改变元素本身，如果从指针角度考虑，
item指针指向item的储存空间（注意不是唯一指针，而是新创建的指针变量，item还有一个属于list的指针），
此时给它赋予新的变量，则这个新产生的指针就“改变方向”，开始指向another_item，也就是说局部变量item的值改变了，
而list内部的指向第N号元素item的指针仍然存在，所以list[i]的值从未改变。
正确的写法是：
```python
for i, item in enumerate(my_list):
    my_list[i] = another_item
```
