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
```

## :two: 变量 类型

```python
# 默认值:         空格隔开   输出换行   屏幕输出(import sys)控制输出缓存(保持False获得较好性能)
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

变量命名-标识符: 字母 数字 _(不可打头) 非关键字/非内置函数

### 数值型

- 整形 `<class 'int'>` None

  大数不会溢出 支持None空值 可用_分隔符(1_000_000) [**0b**二进制Binary  **0o**八进制Octal  **0x**十六进制Hexadecimal ]

- 浮点型 `<class 'float'>`

  科学计数形式都是浮点型值

- 复数 `<class 'complex'>`

  复数运算-`cmath`模块(c-complex) 虚部-j

### 字符串

`<class 'str'>` 注意①引号中的引号`' "  \'  " '`②引号转义`\`③字符串不能直接拼接数值-转换str(x)内置类型/repr(x)函数 (repr以Python表达式形式来表示值 字符串带引号)

Python2.x raw_input() = Python3.x input() 返回str (Python2.x input() 返回对应类型,输入必须正确否则报错-输入字符串必须用引号)

多行注释=长字符串 (可换行 用`\`可转义掉换行) 短字符串和表达式换行必须用`\`转义

r'' 原始字符串

### 字节串

`<class 'bytes'>` 

str -> bytes:

- b''

- bytes('', encoding='utf-8')

- ''.encode('utf-8')

bytes -> str:

- ''.decode('utf-8')

字符集 对同一字符串采用不同字符集会生成不同bytes对象

转义字符 \b退格符 \r回车符

[格式化字符串]: https://github.com/Kukukukiki192/Py/blob/master/codes/02/2.5/format_test.py	"格式化字符串"

  %s 转换说明符(占位符) 