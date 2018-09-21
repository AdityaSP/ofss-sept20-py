Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fp = 'C:\\Users\\Dell lap\\Desktop\\Python\\ofss\\sept20-21\\file1.txt'
>>> print(fp)
C:\Users\Dell lap\Desktop\Python\ofss\sept20-21\file1.txt
>>> fp = 'C:/Users/Dell lap/Desktop/Python/ofss/sept20-21/file1.txt'
>>> print(fp)
C:/Users/Dell lap/Desktop/Python/ofss/sept20-21/file1.txt
>>> fp = 'C:\\Users\\Dell lap\\Desktop\\Python\\ofss\\sept20-21\\file1.txt'
>>> fp
'C:\\Users\\Dell lap\\Desktop\\Python\\ofss\\sept20-21\\file1.txt'
>>> print(fp)
C:\Users\Dell lap\Desktop\Python\ofss\sept20-21\file1.txt
>>> fp = 'D:\newfile.txt
SyntaxError: EOL while scanning string literal
>>> fp = 'D:\newfile.txt'
>>> print(fp)
D:
ewfile.txt
>>> fp = 'D:\\newfile.txt'
>>> print(fp)
D:\newfile.txt
>>> fp = 'C:\\Users\\Dell lap\\Desktop\\Python\\ofss\\sept20-21\\file1.txt'
>>> fp = 'C:/Users/Dell lap/Desktop/Python/ofss/sept20-21/file1.txt'
>>> fp = r'C:\Users\Dell lap\Desktop\Python\ofss\sept20-21\file1.txt'
>>> fp
'C:\\Users\\Dell lap\\Desktop\\Python\\ofss\\sept20-21\\file1.txt'
>>> 
>>> 
>>> 
>>> fh = open(fp,'wt')
>>> s = 'line 1'
>>> fh.write(s)
6
>>> fh.close()
>>> fh.write(s)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    fh.write(s)
ValueError: I/O operation on closed file.
>>> fh = open(fp,'wt')
>>> s = 'line 2'
>>> fh.close()
>>> fh = open(fp,'at')
>>> fh.write('line 1')
6
>>> fh.write('\nline 2')
7
>>> fh.close()
>>> fh = open(fp,'at')
>>> fh.write('\nline 3')
7
>>> fh.close()
>>> 
>>> 
>>> fh = open(fp, 'rt')
>>> fh.write('\nline 3')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    fh.write('\nline 3')
io.UnsupportedOperation: not writable
>>> s = fh.read()
>>> s
'line 1\nline 2\nline 3'
>>> s = fh.read()
>>> s
''
>>> fh.seek(0)
0
>>> s = fh.read()
>>> s
'line 1\nline 2\nline 3'
>>> #li = fh.readlines()
>>> fh.seek(0)
0
>>> li = fh.readlines()
>>> li
['line 1\n', 'line 2\n', 'line 3']
>>> fh.seek(0)
0
>>> for line in fh:
	print(line)

	
line 1

line 2

line 3
>>> 
>>> 
>>> 
>>> 
>>> 
>>> fh.close()
>>> 
>>> 
>>> # context manager
>>> fh = open(fp)
>>> print(fh.read())
line 1
line 2
line 3
>>> fh.close()
>>> with open(fp) as fh:
	print(fh.read())

	
line 1
line 2
line 3
>>> 
