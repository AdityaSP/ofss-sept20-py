Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # String, Lists, Tuples, Diction
>>> a = "Hello World"
>>> type(a)
<class 'str'>
>>> b = "c"
>>> type(b)
<class 'str'>
>>> a + b
'Hello Worldc'
>>> c = a + b
>>> c
'Hello Worldc'
>>> a + 5
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a + 5
TypeError: must be str, not int
>>> '5' + 5
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    '5' + 5
TypeError: must be str, not int
>>> '5' + str(5)
'55'
>>> type(5)
<class 'int'>
>>> int('5') + 5
10
>>> a
'Hello World'
>>> a.islower()
False
>>> 
>>> 
>>> a.upper()
'HELLO WORLD'
>>> a
'Hello World'
>>> a
'Hello World'
>>> a = 'Hello Again'
>>> a
'Hello Again'
>>> a = a.upper()
>>> a
'HELLO AGAIN'
>>> len(a)
11
>>> a[0]
'H'
>>> a[10]
'N'
>>> a[11]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a[11]
IndexError: string index out of range
>>> a[-1]
'N'
>>> a[-5]
'A'
>>> a[-11]
'H'
>>> a[len(a) * -1]
'H'
>>> a[-len(a)]
'H'
>>> a[-12]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a[-12]
IndexError: string index out of range
>>> a
'HELLO AGAIN'
>>> a[0:5]
'HELLO'
>>> a[0:1000]
'HELLO AGAIN'
>>> a[-1:-5]
''
>>> a[-5:-1]
'AGAI'
>>> a[2:-1]
'LLO AGAI'
>>> a[10:-5]
''
>>> a[0:5:1]
'HELLO'
>>> a[-1:-5:1]
''
>>> a[-1:-5:-1]
'NIAG'
>>> a[10:-5:-1]
'NIAG'
>>> a
'HELLO AGAIN'
>>> a[-1:-11:-1]
'NIAGA OLLE'
>>> a[-1:0:-1]
'NIAGA OLLE'
>>> a[-1:-12:-1]
'NIAGA OLLEH'
>>> a[-1: -len(a)-1:-1]
'NIAGA OLLEH'
>>> a
'HELLO AGAIN'
>>> a
'HELLO AGAIN'
>>> a[0:100:2]
'HLOAAN'
>>> a
'HELLO AGAIN'
>>> a[-1: -len(a)-1:-1]
'NIAGA OLLEH'
>>> a[5:100]
' AGAIN'
>>> a[5:]
' AGAIN'
>>> a[0:5]
'HELLO'
>>> a[:5]
'HELLO'
>>> a[:]
'HELLO AGAIN'
>>> a[::]
'HELLO AGAIN'
>>> a[::-1]
'NIAGA OLLEH'
>>> a[-1: -len(a)-1:-1]
'NIAGA OLLEH'
>>> a[::-1]
'NIAGA OLLEH'
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> a
'HELLO AGAIN'
>>> a[:5]
'HELLO'
>>> a[1:2]
'E'
>>> s = 'The discovery of India'
>>> s.split()
['The', 'discovery', 'of', 'India']
>>> s = 'one,two,three'
>>> s.split(',')
['one', 'two', 'three']
>>> s = 'The discovery of India'
>>> s.split()
['The', 'discovery', 'of', 'India']
>>> s.split(" ")
['The', 'discovery', 'of', 'India']
>>> s = '1  2'
>>> s.split()
['1', '2']
>>> s.split(" ")
['1', '', '2']
>>> s = "1\t\n2"
>>> s.split()
['1', '2']
>>> s
'1\t\n2'
>>> print(s)
1	
2
>>> s = 'The discovery of India'
>>> s.split()
['The', 'discovery', 'of', 'India']
>>> x = s.split()
>>> type(x)
<class 'list'>
>>> type(s.split())
<class 'list'>
>>> type(x = s.split())
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    type(x = s.split())
TypeError: type() takes 1 or 3 arguments
>>> 
