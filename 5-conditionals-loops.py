Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 8
>>> if a < 10:
	print("Single digit")

	
Single digit
>>> a = 10
>>> if a < 10:
	print("Single digit")
else:
	print("May be double digit")

	
May be double digit
>>> a = 100
>>> if a < 10:
	print("1 Digit")
elif a < 100:
	print("2 Digits")
else:
	print("2+ digits")

	
2+ digits
>>> a < 100
False
>>> li = ['India','China','UK']
>>> if 'India' in li:
	print("Found")

	
Found
>>> s = 'http://google.com'
>>> 'http' in s
True
>>> x = 3
>>> y = 10
>>> x > 0 and x < 5
True
>>> 0 < x < 5
True
>>> x > 0 and x < y and y < 20
True
>>> 0 < x < y < 20
True
>>> x < 2 or y < 20
True
>>> x < 2
False
>>> not x < 2
True
>>> 
================ RESTART: C:/Users/Dell lap/Desktop/trial.py ================
Hello World!
>>> s
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> a = 'hello'
>>> a + 5
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a + 5
TypeError: must be str, not int
>>> a * 5
'hellohellohellohellohello'
>>> 
>>> 
>>> 
>>> li = ['ka','up','tn','mp']
>>> count = 0
>>> while count < len(li):
	print(li[count])
	count += 1

	
ka
up
tn
mp
>>> while count < len(li):
	print(li[count])
	count += 1

	
>>> count
4
>>> count = 0
>>> while count < len(li):
	print(li[count])
	count += 1

	
ka
up
tn
mp
>>> li
['ka', 'up', 'tn', 'mp']
>>> for code in li:
	print(code)

	
ka
up
tn
mp
>>> import random
>>> random.randint(1,100)
54
>>> 
