Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> d = { "name": "Aditya", "email": "sp.aditya@gmail.com" }
>>> len(d)
2
>>> d['name']
'Aditya'
>>> d['email']
'sp.aditya@gmail.com'
>>> d['city']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d['city']
KeyError: 'city'
>>> d['city'] ='Bangalore'
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'Bangalore'}
>>> d['city'] ='Mysore'
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'Mysore'}
>>> 'name' in d
True
>>> d.keys()
dict_keys(['name', 'email', 'city'])
>>> d.values()
dict_values(['Aditya', 'sp.aditya@gmail.com', 'Mysore'])
>>> d.keys()[1]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d.keys()[1]
TypeError: 'dict_keys' object does not support indexing
>>> list(d.keys())
['name', 'email', 'city']
>>> for ky in d.keys():
	print(ky)

	
name
email
city
>>> 'Mysore' in d.values()
True
>>> d['phone'] = ['12312345234', '12345341546']
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'Mysore', 'phone': ['12312345234', '12345341546']}
>>> d['phone'][-1]
'12345341546'
>>> d['address'] = {'home': 'asdkfjlja', 'work': 'asdkfjouew'}
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'Mysore', 'phone': ['12312345234', '12345341546'], 'address': {'home': 'asdkfjlja', 'work': 'asdkfjouew'}}
>>> d['address']['home']
'asdkfjlja'
>>> d.items()
dict_items([('name', 'Aditya'), ('email', 'sp.aditya@gmail.com'), ('city', 'Mysore'), ('phone', ['12312345234', '12345341546']), ('address', {'home': 'asdkfjlja', 'work': 'asdkfjouew'})])
>>> for item in d.items():
	print("k", item[0], "v", item[1])

	
k name v Aditya
k email v sp.aditya@gmail.com
k city v Mysore
k phone v ['12312345234', '12345341546']
k address v {'home': 'asdkfjlja', 'work': 'asdkfjouew'}
>>> for k,v in d.items():
	print("k", k, "v", v)

	
k name v Aditya
k email v sp.aditya@gmail.com
k city v Mysore
k phone v ['12312345234', '12345341546']
k address v {'home': 'asdkfjlja', 'work': 'asdkfjouew'}
>>> a,b = ("India",'China')
>>> a
'India'
>>> b
'China'
>>> k,v = ('name', 'Aditya')
>>> k
'name'
>>> v
'Aditya'
>>> 
