Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> #REPL - Read Evaluate Print Loop
>>> print("Hello World!")
Hello World!
>>> print("Hello World!", "Hello OFSS")
Hello World! Hello OFSS
>>> print('Hello World!')
Hello World!
>>> print("""Hello World""")
Hello World
>>> print('''Hello World''')
Hello World
>>> print('Hello World
      
SyntaxError: EOL while scanning string literal
>>> print('Hello World \
Hello OFSS')
Hello World Hello OFSS
>>> print('''Hello World
Hello OFSS''')
Hello World
Hello OFSS
>>> 
>>> 
>>> #int a = 10
>>> a = 10
>>> b = 12.3
>>> c = 'Hello'
>>> d = True
>>> print(a)
10
>>> a
10
>>> type(a)
<class 'int'>
>>> type(b), type(c), type(d)
(<class 'float'>, <class 'str'>, <class 'bool'>)
>>> #int a = 10 --- Strongly typed and statically typed eg.C
>>> #a = 10 ----- Strongly typed and dynamic PG eg. Python
>>> a = c
>>> type(a)
<class 'str'>
>>> 
>>> 
>>> a = 1000
>>> id(a)
911594202384
>>> a = c
>>> id(a)
911597022656
>>> a = 1000
>>> id(a)
911594204048
>>> 
>>> a = 10
>>> id(a)
1477665280
>>> a = c
>>> id(a)
911597022656
>>> a = 10
>>> id(a)
1477665280
>>> 10 + 10
20
>>> 10 + 3.4
13.4
>>> 3/4
0.75
>>> if a/b == 0:
	print("Launch Rocket")

	
>>> 
