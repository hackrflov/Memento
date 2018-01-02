+ arrayObject.slice(start, end): 从已有的数组中返回选定的元素
+ arrayObject.push(element): 将新元素添加到一个数组中，并返回数组的新长度值


data type
---------
1. dict is also object, you can use `obj.key` or `obj['key']` to access property

common bugs
-----------
1. 如果写的event handler针对的是还没有加载的内容，则会失效。正确的方法应该在新的元素添加到DOM中之后再bind.
