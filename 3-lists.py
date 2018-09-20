Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> li = list()
>>> li
[]
>>> li = []
>>> li
[]
>>> li = ['India','Japan','China']
>>> len(li)
3
>>> li[0]
'India'
>>> li[5]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    li[5]
IndexError: list index out of range
>>> li[-1]
'China'
>>> li[::-1]
['China', 'Japan', 'India']
>>> # any datatype
>>> # Not an array implementation
>>> li
['India', 'Japan', 'China']
>>> li[1]='USA'
>>> li
['India', 'USA', 'China']
>>> s = 'hello'
>>> s[0]='H'
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s[0]='H'
TypeError: 'str' object does not support item assignment
>>> id(li)
398440513480
>>> li[-1]='UK'
>>> li
['India', 'USA', 'UK']
>>> id(li)
398440513480
>>> li
['India', 'USA', 'UK']
>>> li.append('Cuba')
>>> li
['India', 'USA', 'UK', 'Cuba']
>>> b = ['SL','Brazil','Canada']
>>> li.extend(b)
>>> li
['India', 'USA', 'UK', 'Cuba', 'SL', 'Brazil', 'Canada']
>>> li = ['India', 'USA', 'UK']
>>> b
['SL', 'Brazil', 'Canada']
>>> li.append(b)
>>> li
['India', 'USA', 'UK', ['SL', 'Brazil', 'Canada']]
>>> len(li)
4
>>> li[-1]
['SL', 'Brazil', 'Canada']
>>> li[-1][-1]
'Canada'
>>> li[-1][-1][-1][-1][-1][-1]
'a'
>>> li = ['India', 'USA', 'UK']
>>> li.extend('Afghanistan')
>>> li
['India', 'USA', 'UK', 'A', 'f', 'g', 'h', 'a', 'n', 'i', 's', 't', 'a', 'n']
>>> len(li)
14
>>> li = ['India', 'USA', 'UK']
>>> li.insert(1,'Russia')
>>> li
['India', 'Russia', 'USA', 'UK']
>>> li.insert(0,'Bangalore')
>>> li.insert(100,'Bangalore')
>>> li
['Bangalore', 'India', 'Russia', 'USA', 'UK', 'Bangalore']
>>> li.insert(-1, 'Thailand')
>>> li
['Bangalore', 'India', 'Russia', 'USA', 'UK', 'Thailand', 'Bangalore']
>>> li.remove('Bangalore')
>>> li
['India', 'Russia', 'USA', 'UK', 'Thailand', 'Bangalore']
>>> 
>>> 
>>> b
['SL', 'Brazil', 'Canada']
>>> del b
>>> b
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> li
['India', 'Russia', 'USA', 'UK', 'Thailand', 'Bangalore']
>>> del li[3]
>>> li
['India', 'Russia', 'USA', 'Thailand', 'Bangalore']
>>> li.pop()
'Bangalore'
>>> li
['India', 'Russia', 'USA', 'Thailand']
>>> li.pop(1)
'Russia'
>>> li
['India', 'USA', 'Thailand']
>>> x = li.pop()
>>> li
['India', 'USA']
>>> x
'Thailand'
>>> 

>>> li  =['abc', 'eee', 'bcd', 'cde', 'edf', ['india', 'uk'], 'kkk', 'uk']
>>> li.remove('india')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    li.remove('india')
ValueError: list.remove(x): x not in list
>>> li[-3]
['india', 'uk']
>>> li[-3].remove('india')
>>> li
['abc', 'eee', 'bcd', 'cde', 'edf', ['uk'], 'kkk', 'uk']
>>> li = ['India', 'USA', 'Thailand', 'New Zealand']
>>> li[-1].split()[-1]
'Zealand'
>>> li[-1].split()[-1].upper()
'ZEALAND'
>>> 
