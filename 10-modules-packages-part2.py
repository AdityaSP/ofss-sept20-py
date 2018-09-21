Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.path
['', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\Lib\\idlelib', 'C:\\Users\\Dell lap\\Desktop\\Python\\ofss\\sept20-21\\modules', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\python36.zip', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\DLLs', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\site-packages']
>>> import calc
>>> calc.add(4,5)
In module calc.py something else
9
>>> import db.config
>>> import network.config
>>> db.config.configure()
Dummy db configuration
>>> network.config.configure()
Dummy network configuration
>>> 
>>> 
>>> 
>>> import db.config as dbc
>>> dbc.configure()
Dummy db configuration
>>> import nw.config as nwc
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    import nw.config as nwc
ModuleNotFoundError: No module named 'nw'
>>> import network.config as nwc
>>> nwc.configure()
Dummy network configuration
>>> 
>>> 
>>> from db.config import configure
>>> configure()
Dummy db configuration
>>> from network.config import configure
>>> configure()
Dummy network configuration
>>> from db.config import *
>>> configure()
Dummy db configuration
>>> def sub(x,y):
	return x - y

>>> from network.config import *
>>> sub(5,6)
-1
>>> from threading import Thread
>>> 
>>> 
