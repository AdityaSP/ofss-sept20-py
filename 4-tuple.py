Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a_t = ('India','China','UK')
>>> type(a_t)
<class 'tuple'>
>>> a_t[1]
'China'
>>> a_t[-1]
'UK'
>>> a_t[::-1]
('UK', 'China', 'India')
>>> a_t[0]='SL'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a_t[0]='SL'
TypeError: 'tuple' object does not support item assignment
>>> a_t = 'India','China', 'UK'
>>> type(a_t)
<class 'tuple'>
>>> a_t
('India', 'China', 'UK')
>>> a_t
('India', 'China', 'UK')
>>> a,b,c = a_t
>>> a
'India'
>>> b
'China'
>>> c
'UK'
>>> a,b = a_t
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a,b = a_t
ValueError: too many values to unpack (expected 2)
>>> a
'India'
>>> b
'China'
>>> a,b = b,a
>>> a
'China'
>>> b
'India'
>>> t = ('India')
>>> type(t)
<class 'str'>
>>> li = ['India']
>>> li
['India']
>>> type(li)
<class 'list'>
>>> t = tuple(li)
>>> type(t)
<class 'tuple'>
>>> len(t)
1
>>> t
('India',)
>>> t = ('India',)
>>> type(t)
<class 'tuple'>
>>> len(t)
1
>>> t
('India',)
>>> 
>>> ['india',]
['india']
>>> tuple(['india',])
('india',)
>>> type(tuple(['india',]))
<class 'tuple'>
>>> len(tuple(['india',]))
1
>>> 
>>> 
>>> t = ([1,2,3],[4,5,6])
>>> li = [(1,2,3), (4,5,6)]
>>> li.appen(4)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    li.appen(4)
AttributeError: 'list' object has no attribute 'appen'
>>> li.append(4)
>>> li
[(1, 2, 3), (4, 5, 6), 4]
>>> li[1][1]=3
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    li[1][1]=3
TypeError: 'tuple' object does not support item assignment
>>> li.pop(1)
(4, 5, 6)
>>> li
[(1, 2, 3), 4]
>>> t = ([1,2,3],[4,5,6])
>>> t[0].pop()
3
>>> t
([1, 2], [4, 5, 6])
>>> t[0].pop()
2
>>> t[0].pop()
1
>>> t
([], [4, 5, 6])
>>> 
