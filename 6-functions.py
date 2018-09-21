Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sayhi():
	print("Hi")

	
>>> sayhi()
Hi
>>> len('hello')
5
>>> len('hello') * 5
25
>>> def sayhi():
	print("Hi")
	return "Hi"

>>> x = sayhi()
Hi
>>> x
'Hi'
>>> def sayhi():
	return "Hi"

>>> x = sayhi()
>>> s = "Hello"
>>> s.upper()
'HELLO'
>>> x = s.upper()
>>> s
'Hello'
>>> x
'HELLO'
>>> l= []
>>> l.append(4)
>>> l
[4]
>>> def sayhi():
	return "Hi"

>>> def full_name(fn, ln):
	return fn + " " + ln

>>> full_name('Aditya', 'Prabhakara')
'Aditya Prabhakara'
>>> x = full_name('Aditya', 'Prabhakara')
>>> full_name('Prabhakara', 'Aditya')
'Prabhakara Aditya'
>>> full_name(fn='Aditya', ln = 'Prabhakara')
'Aditya Prabhakara'
>>> full_name(ln = 'Prabhakara', fn='Aditya')
'Aditya Prabhakara'
>>> def full_name(fn, ln, title='mr'):
	return title.capitalize()+ "." + fn + " " + ln

>>> full_name('Aditya','Prabhakara')
'Mr.Aditya Prabhakara'
>>> full_name('Aditya','Prabhakara', 'dr')
'Dr.Aditya Prabhakara'
>>> li = [67,123,78,23,890,34]
>>> li
[67, 123, 78, 23, 890, 34]
>>> sorted(li)
[23, 34, 67, 78, 123, 890]
>>> li
[67, 123, 78, 23, 890, 34]
>>> sorted(li)[::-1]
[890, 123, 78, 67, 34, 23]
>>> sorted(li, reverse=True)
[890, 123, 78, 67, 34, 23]
>>> a = None
>>> type(None)
<class 'NoneType'>
>>> id(None)
1477940432
>>> if a:
	print("hs something")
else:
	print("a is nothing")

	
a is nothing
>>> li = []
>>> 
>>> if len(li) > 0:
	print("its not empty")

	
>>> s = ""
>>> if len(s) > 0:
	print("its not empty")

	
>>> #None, False, 0, "", [],(), {}
>>> if li:
	print("its not empty")

	
>>> li.append(10)
>>> if li:
	print("its not empty")

	
its not empty
>>> # function as first class citizens or first class constructs or first class objects
>>> def sayhi():
	print("Hi")

	
>>> a = 10
>>> type(a)
<class 'int'>
>>> type(sayhi)
<class 'function'>
>>> id(a)
1478386176
>>> id(sayhi)
1086828706400
>>> b = a
>>> type(b)
<class 'int'>
>>> greet = sayhi
>>> type(greet)
<class 'function'>
>>> b + 10
20
>>> greet()
Hi
>>> id(greet)
1086828706400
>>> id(sayhi)
1086828706400
>>> del sayhi
>>> sayhi()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    sayhi()
NameError: name 'sayhi' is not defined
>>> def sayhi():
	"this is a cheerful function which says Hi"
	print("Hi")

	
>>> sayhi.__doc__
'this is a cheerful function which says Hi'
>>> len.__doc__
'Return the number of items in a container.'
>>> sorted.__doc__
'Return a new list containing all items from the iterable in ascending order.\n\nA custom key function can be supplied to customize the sort order, and the\nreverse flag can be set to request the result in descending order.'
>>> #dunder
>>> 
