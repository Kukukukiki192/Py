# Py

源码基于<疯狂Python讲义>学习补充

## :one: 概述 开发环境

cmd / wt 使用py命令

```python
>python xx.py # 执行文件
>python # 启动交互式解释器
>>>  ... # 缩进不对会编译报错IndentationError: unexpected indent
>>> exit() / ctrl+z # 退出
>>> 2**3 # 计算器
# 输出变量类型
>>> type(a)
<class '...'>
# 查看关键字
>>> import keyword
>>> keyword.kwlist
# 查看内置函数
>>> dir(__builtins__) # 或:
>>> import builtins
>>> dir(builtins)
>>> dir(类) # 查看某个类所有方法
>>> help(类.方法) # 查看方法的用法
```

## :two: 变量 类型

<a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.2/print_test.py">变量输出</a>

```python
# 默认值:         空格隔开   输出换行   屏幕输出(import sys)控制输出缓存(保持False获得较好性能)
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

变量命名-标识符: 字母 数字 _(不可打头) 非关键字/非内置函数

### 数值型

1. <a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.3/integer_test.py">整形</a> `<class 'int'>`

   大数不会溢出 支持None空值 可用_分隔符(1_000_000) <a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.3/hex_test.py">[**0b**二进制Binary  **0o**八进制Octal  **0x**十六进制Hexadecimal]</a> 

2. <a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.3/float_test.py">浮点型</a> `<class 'float'>`

   科学计数形式都是浮点型值

3. <a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.3/complex_test.py">复数</a> `<class 'complex'>`

   复数运算-`cmath`模块(c-complex) 虚部-j

### 字符串

`<class 'str'>` 

- 注意:①引号中的引号`' "  \'  " '`②引号转义`\`<a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.4/to_string.py">③</a>字符串不能直接拼接数值-转换str(x)内置类型/repr(x)函数 (repr以Python表达式形式来表示值 字符串带引号)

- <a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.4/input_test.py">变量输入</a>: Python2.x raw_input() = Python3.x input() 返回str (Python2.x input() 返回对应类型,输入必须正确否则报错-输入字符串必须用引号) 

- 多行注释=<a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.4/long_str.py">长字符串</a> (可换行 用`\`可转义掉换行) 短字符串和表达式换行必须用`\`转义

- r'' <a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.4/raw_str.py">原始字符串</a> 

- <a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.5/escape_char.py">转义字符</a>: \b退格符 \r回车符 \n换行符

- <a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.5/format_test.py">字符串格式化</a>: %s 转换说明符(占位符)  多个占位符`print("%s is a %s years old boy" % (user, age))`

  **字符串格式化不支持%b二进制形式输出,只能用bin()转换**

   <img src="C:\Users\K\AppData\Roaming\Typora\typora-user-images\image-20221206102137668.png" alt="image-20221206102137668" style="zoom:33%;" />

- <a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.5/str_method.py">字符串方法</a>:索引 in运算 len() min/max() 字母大小写 等

### <a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.4/bytes_test.py">字节串</a>

`<class 'bytes'>`  字符集:对同一字符串采用不同字符集会生成不同bytes对象

```python
# str -> bytes
b''
bytes('', encoding='utf-8')
''.encode('utf-8')
# bytes -> str
''.decode('utf-8')
```

### <a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.6">运算符</a>

赋值/扩展赋值运算符	<a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.6/arithmetic.py">算数运算符</a>(复杂运算引入math模块)	索引运算符`s[开始: 结束 :间隔(步长)]`

比较运算符(`==/!=` 比较内容  `is/is not` 比较对象)	逻辑运算符`and or not`	<a href="https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.6/ternary_operator_test.py">三目运算符</a>(True_statements可放置多条语句,支持2种执行方式: `,`隔开返回多条语句返回值组合成元组 `;`隔开只返回第一条语句返回值)	in运算符	

## :three: 列表 元组 字典

