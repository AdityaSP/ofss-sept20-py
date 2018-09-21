Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import calc
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import calc
ModuleNotFoundError: No module named 'calc'
>>> import sys
>>> sys.path
['', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\Lib\\idlelib', 'E:\\todel', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\python36.zip', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\DLLs', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\site-packages']
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> random.__file__
'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\random.py'
>>> sys.path.append('C:\\Users\\Dell lap\\Desktop\\Python\\ofss\\sept20-21')
>>> sys.path
['', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\Lib\\idlelib', 'E:\\todel', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\python36.zip', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\DLLs', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\site-packages', 'C:\\Users\\Dell lap\\Desktop\\Python\\ofss\\sept20-21']
>>> sys.path.pop()
'C:\\Users\\Dell lap\\Desktop\\Python\\ofss\\sept20-21'
>>> sys.path.append('C:\\Users\\Dell lap\\Desktop\\Python\\ofss\\sept20-21\\modules')
>>> sys.path
['', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\Lib\\idlelib', 'E:\\todel', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\python36.zip', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\DLLs', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\site-packages', 'C:\\Users\\Dell lap\\Desktop\\Python\\ofss\\sept20-21\\modules']
>>> import calc
>>> calc.add(45,77)
In module calc.py
122
>>> dir(calc)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add']
>>> calc.__file__
'C:\\Users\\Dell lap\\Desktop\\Python\\ofss\\sept20-21\\modules\\calc.py'
>>> import calc
>>> calc.add(45,77)
In module calc.py
122
>>> importlib.reload(calc)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    importlib.reload(calc)
NameError: name 'importlib' is not defined
>>> import importlib
>>> importlib.reload(calc)
<module 'calc' from 'C:\\Users\\Dell lap\\Desktop\\Python\\ofss\\sept20-21\\modules\\calc.py'>
>>> calc.add(45,77)
In module calc.py something else
122
>>> 
