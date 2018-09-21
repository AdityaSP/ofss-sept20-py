Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sayhi():
	return "Hi"

>>> def add(x,y):
	return x + y

>>> a = 10
>>> b = 20
>>> add(a,b)
30
>>> def someexec(f):
	print(type(f))

	
>>> someexec(a)
<class 'int'>
>>> someexec(sayhi)
<class 'function'>
>>> def someexec(f):
	x = f()
	return x

>>> someexec(sayhi)
'Hi'
>>> # first order function
>>> # Higer order function -(partial def) - a function accepting a function
>>> kms = [5,10,21,42]
>>> mi = []
>>> for km in kms:
	m = km * 0.62
	mi.append(m)

	
>>> mi
[3.1, 6.2, 13.02, 26.04]
>>> def kmtomi(x):
	return x * 0.62

>>> kmtomi(5)
3.1
>>> map(kmtomi, kms)
<map object at 0x0000003C0AC184A8>
>>> mo = map(kmtomi, kms)
>>> for m in mo:
	print(m)

	
3.1
6.2
13.02
26.04
>>> mi = list(map(kmtomi, kms))
>>> mi
[3.1, 6.2, 13.02, 26.04]
>>> kms = [5,10,21,42]
>>> mi = []
>>> for km in kms:
	m = km * 0.62
	mi.append(m)

	
>>> mi
[3.1, 6.2, 13.02, 26.04]
>>> def kmtomi(x):
	return x * 0.62

>>> mi = list(map(kmtomi, kms))
>>> mi
[3.1, 6.2, 13.02, 26.04]
>>> def mitokm(x):
	return x / 0.62

>>> list(map(mitokm, map(kmtomi, kms)))
[5.0, 10.0, 21.0, 42.0]
>>> 
>>> 
>>> 
>>> x = 40
>>> y = 50
>>> add(x,y)
90
>>> add(40,50)
90
>>> 40
40
>>> "Hello"
'Hello'
>>> # function literals or anonymous functions
>>> def add(x,y):
	return x + y

>>> lambda x,y: x+y
<function <lambda> at 0x0000003C0AC10730>
>>> f = lambda x,y: x+y
>>> f(10,20)
30
>>> list(map(lambda x: x *0.62 , kms))
[3.1, 6.2, 13.02, 26.04]
>>> kms
[5, 10, 21, 42]
>>> list(map(lambda x: x *0.62 , kms))
[3.1, 6.2, 13.02, 26.04]
>>> li = [34,56,12,67,89]
>>> sum(li)
258
>>> s = '12,45,123,567,123,56,78'
>>> s.split(',')
['12', '45', '123', '567', '123', '56', '78']
>>> int('12')
12
>>> sum(map(lambda x : int(x), s.split(',')))
1004
>>> sum(map(int, s.split(',')))
1004
>>> s = '12,45,123,567,123,56,78'
>>> sum(map(int, s.split(',')))
1004
>>> sayhi()
'Hi'
>>> def greet():
	return sayhi()

>>> greet()
'Hi'
>>> sayhi()
'Hi'
>>> s = 'how are you, what do you do, where are you'
>>> len(s.split())
10
>>> li = ['Ahmedabad', 'agra', 'Bangalore','baroda', 'zurich']
>>> sorted(li)
['Ahmedabad', 'Bangalore', 'agra', 'baroda', 'zurich']
>>> li = ['Ahmedabad', 'agra', 'Bangalore','baroda', 'Zurich']
>>> sorted(li)
['Ahmedabad', 'Bangalore', 'Zurich', 'agra', 'baroda']
>>> sorted(map(lambda x : x.lower(), li))
['agra', 'ahmedabad', 'bangalore', 'baroda', 'zurich']
>>> 
>>> 
>>> sorted(li, key = lambda x : x.lower())
['agra', 'Ahmedabad', 'Bangalore', 'baroda', 'Zurich']
>>> li = ['Ahmedabad', 'agra', 'Bangalore','baroda', 'zurich']
>>> sorted(li, key=len)
['agra', 'baroda', 'zurich', 'Ahmedabad', 'Bangalore']
>>> li = ['Virat Kohli','MS Dhoni','R Ashwin', 'Murali Karthik','KL Rahul']
>>> sorted(li, key = lambda x : x.split()[-1])
['R Ashwin', 'MS Dhoni', 'Murali Karthik', 'Virat Kohli', 'KL Rahul']
>>> age = [12,45,23,89,23,78,90]
>>> filter(lambda x : 20<x<80, age)
<filter object at 0x0000003C0AC27470>
>>> list(filter(lambda x : 20<x<80, age))
[45, 23, 23, 78]
>>> 
>>> 
>>> 
>>> def greet(name):
	def sayhi():
		return "Hi" + " " + name
	return sayhi

>>> x = greet('Aditya')
>>> y = greet('Arun')
>>> type(x), type(y)
(<class 'function'>, <class 'function'>)
>>> x()
'Hi Aditya'
>>> y()
'Hi Arun'
>>> # Higer order function - a function with either accepts a function or returns back a function
>>> def bill(x,y, tax):
	total = x + y
	grandtotal = total + total * tax
	return grandtotal

>>> bill(10,20, .18)
35.4
>>> def bill(x,y):
	total = x +y
	def withtax(tax):
		return total + total * tax
	return withtax

>>> bill1 = bill(100,200)
>>> bill1(.18)
354.0
>>> bill2 = bill(10,20)
>>> bill3 = bill(200,34)
>>> bill2(.10)
33.0
>>> bill3(.10)
257.4
>>> bill(10,20)(.10)
33.0
>>> #Higher order function: closures, partial functions
>>> 
>>> 
>>> 
>>> kms = [5,10,21,42]
>>> mi = []
>>> for km in kms:
	m = km * 0.62
	mi.append(m)

	
>>> mi
[3.1, 6.2, 13.02, 26.04]
>>> mi = list(map(lambda x : x * 0.62, kms))
>>> mi
[3.1, 6.2, 13.02, 26.04]
>>> #mi = [<expression> <for statement> <filter gate>]
>>> mi = [ km * 0.62 for km in kms]
>>> mi
[3.1, 6.2, 13.02, 26.04]
>>> age
[12, 45, 23, 89, 23, 78, 90]
>>> # ages in the range of 20 to 80 returned back as months
>>> list(map(lambda x : x * 12, filter(lambda x : 20 < x < 80, age)))
[540, 276, 276, 936]
>>> [ x*12 for a in age if 20 < x< 80]
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    [ x*12 for a in age if 20 < x< 80]
  File "<pyshell#150>", line 1, in <listcomp>
    [ x*12 for a in age if 20 < x< 80]
TypeError: '<' not supported between instances of 'int' and 'function'
>>> [ a*12 for a in age if 20 < a< 80]
[540, 276, 276, 936]
>>> list(map(lambda x : x * 12, filter(lambda x : 20 < x < 80, age)))
[540, 276, 276, 936]
>>> [ a*12 for a in age if 20 < a< 80]
[540, 276, 276, 936]
>>> #7 +4 = 11
>>> #7
>>> 
