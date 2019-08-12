# python 自我总结

## _本笔记记录了关于本人的 python 所学的知识汇总_

---

### python2 和 python3 的语法问题

python:
v2 `print "hello world"` == v3 `print ("hello world")`
v2 `raw_input()` == v3 `input()`

---

###列表

`cmp(list1, list2)`
比较两个列表的元素

`len(list)`
列表元素个数

`max(list)`
返回列表元素最大值

`min(list`)
返回列表元素最小值
`list(seq)`
将元组转换为列表

`list.append(obj)`
在列表末尾添加新的对象

`list.count(obj)`
统计某个元素在列表中出现的次数

`list.extend(seq)`
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

`list.index(obj)`
从列表中找出某个值第一个匹配项的索引位置

`list.insert(index, obj)`
将对象插入列表

`list.pop([index=-1])`
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

`list.remove(obj)`
移除列表中某个值的第一个匹配项

`list.reverse()`
反向列表中元素

`list.sort(cmp=None, key=None, reverse=False)`
对原列表进行排序

---

### 字典

`cmp(dict1, dict2)`
比较两个字典元素。

`len(dict)`
计算字典元素个数，即键的总数。

`str(dict)`
输出字典可打印的字符串表示。

`type(variable)`
返回输入的变量类型，如果变量是字典就返回字典类型。

`dict.clear()`
删除字典内所有元素

`dict.copy()`
返回一个字典的浅复制

`dict.fromkeys(seq[, val])`
创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值

`dict.get(key, default=None)`
返回指定键的值，如果值不在字典中返回 default 值

`dict.has_key(key)`
如果键在字典 dict 里返回 true，否则返回 false

`dict.items()`
以列表返回可遍历的(键, 值) 元组数组

`dict.keys()`
以列表返回一个字典所有的键

`dict.setdefault(key, default=None)`
和 get()类似, 但如果键不存在于字典中，将会添加键并将值设为 default

`dict.update(dict2)`
把字典 dict2 的键/值对更新到 dict 里

`dict.values()`
以列表返回字典中的所有值

`pop(key[,default])`
删除字典给定键 key 所对应的值，返回值为被删除的值。key 值必须给出。 否则，返回 default 值。

`popitem()`
随机返回并删除字典中的一对键和值。

---

### 时间

---

### 函数

#### 全局变量和局部变量

定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。

局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。如下实例：

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

total = 0; # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2; # total在这里是局部变量.
   print "函数内是局部变量 : ", total
   return total;

#调用sum函数
sum( 10, 20 );
print "函数外是全局变量 : ", total
```

**_<u>当需要在函数内用到全局变量时:</u>_**

<!--利用global声明这是个全局变量-->

```python
total = 0; # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
   global total
   total = arg1 + arg2; # total在这里是 全局变量.
   return


```

#### 不定长函数

加了星号（\*）的变量名会存放所有未命名的变量参数。不定长参数实例如下：

```python

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print var
   return;

# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );

```

#### 可变对象和不可变对象

......

---

### 模块
