```javascript
$(document).ready( function() { 
    // init code
});

// To use get
$.get( "ajax/test.html", function( data ) {
  $( ".result" ).html( data );
  alert( "Load was performed." );
});

// To use ajax
$.ajax({
    url: url,
    method: 'GET', // also POST, GET, PUT...
    success: function(data) {
        // deal with fetched data
    },
    fail: function(msg) {
        // deal with failed msg
    }
}).done(function() {
    // do something after ajax
}).fail(function() {
    // deal with errors when starting
})

// load page partially
$(selector).load(URL,data,callback);
```

### 获取和设置
- `$(e).attr(name)`: 获取HTML属性
- `$(e).attr(name, value)`: 设置HTML属性
- `$(e).data(name)`: 获取data-*的html标签值
- `$(e).data(name, value)`: 设置data-*的html标签值
- `$(e).css(name)`: 获取css属性
- `$(e).css(name, value)`: 设置css属性
- `$(e).html()`: 获取HTML标签
- `$(e).html(value)`: 设置HTML标签
- `$(e).text()`: 获取文本
- `$(e).text(value)`: 设置文本
- `$(e).val()`: 获取表单控件值(input/select/textarea)
- `$(e).val(value)`: 设置表单控件值((input/select/textarea)
- `$(e).addClass(value)`: 添加类名
- `$(e).hasClass(value)`: 检查是否包含类名
- `$(e).removeClass(value)`: 删除指定类名
- `$(e).toggleClass(value)`: 添加/删除-切换指定类名
- `$(e).removeAttr(value)`: 删除指定属性

### 遍历节点
- `$(e).parent(filter)`: 符合条件的直接父元素
- `$(e).parents(filter)`: 符合条件的所有租先元素
- `$(e).children(filter)`: 符合条件的直接子元素
- `$(e).find(filter)`: 符合条件的所有后代元素
- `$(e).siblings(filter)`: 符合条件的所有同胞元素
- `$(e).next(filter)`: 符合条件的下一个同胞元素
- `$(e).nextAll(filter)`: 符合条件的所有跟随同胞元素
- `$(e).prev(filter)`: 符合条件的上一个同胞元素
- `$(e).prevAll(filter)`: 符合条件的所有前置同胞元素
- `$(e).first()`: 组内第一个元素
- `$(e).last()`: 组内最后一个元素

### 动态效果
- `$(e).hide()`: 隐藏
- `$(e).show()`: 显示
- `$(e).toggle()`: 隐藏/显示切换

### 事件绑定
```javascript
$(e).click(function(e) {
    e.preventDefault();
});
```

### 结构
```javascript
$(e).each(function() {
    // do with $(this)
});
```

### 功能
- `$.param(params)`: 把dict参数转化为url参数格式
