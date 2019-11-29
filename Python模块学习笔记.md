### Python模块学习笔记

#### json模块学习

JSON (JavaScript Object Notation) ,JavaScript对象标记,通过对象和数组的组合来表示数据,是一种轻量级的数据交换格式。

##### 对象和数组

- 数组：数组在JavaScript中是方括号`[]`包裹起来的内容,数据结构为`[ "java","javascript"]`的索引结构。在JavaScript中,数组是一种比较特殊的数据类型,它也可以像对象那样使用键值对,但还是索引用得多。值的类型可以是任意类型。

- 对象: 使用花括号`{}`的内容. 数据结构为:`{key1:values1}`的键值对结构.

  key为对象属性,value为对应的值. 键名使用整数和字符串表示,值的类型可以是任意类型.

##### 处理json数据

Python可以使用json模块实现json文件的读写操作.

1. json读写操作方法
   - 使用json模块的`loads()`方法将json文本字符串转为json对象.
   - 使用json模块的`dumps()`方法将json对象转为文本字符串.

**注意: JSON的数据需要用双引号来包围,不能使用单引号.**

2. 从json文本中读取内容,需要先将文本文件内容读出,然后再利用`loads()`方法转化.

   **注意: 读取json文件时,直接使用loads函数会报如下错误:`TypeError: the JSON object must be str, bytes or bytearray, not 'TextIOWrapper'`,  使用loads方法时,先用read读取json数据,再用loads方法转化.**

   ```python
   str = f.read()
   data = json.loads(str)
   print(data)
   ```

3. json的load和loads方法的区别:

   - `load()`方法: 直接读取json并处理.
   - `loads()`方法: `loads()`需要先用`read()`方法读取,然后再用`loads()`方法转化.

