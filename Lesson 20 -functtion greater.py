Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #create a function that takes 3 numbers and return the greates
>>> #greatest of the 3
>>> #a>b a>c a
>>> #b>a b>c b
>>> #c>a c>b c
>>> 
>>> def greater (a,b,c):
	if a>b and a>c:
		return a
	if b>a and b>c:
		return b
	else:
		return c

	
>>> #a is greatergreater (3,2,1)
>>> greater (3,2,1)
3
>>> #b is greater
>>> greater (2,3,1)
3
>>> #c is greater
>>> greater (1,2,3)
3
>>> 