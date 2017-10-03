#first capital letter
a = 'hello'.capitalize()
print(a)

#caseless
a = 'hEllO'.casefold()
print(a)

#both padding 
a = 'iamhere'.center(100)
print(a)

#substring occurrence
a = 'i am a i am a good goof person'.count('am')
print(a)

a = 'hello'
print(a.endswith('o'))

#index of substring
a = 'find a substring from me'
print(a.find('from'))  # no error
print(a.index('from')) # ValueError

#format
print("The sum of 1 + 2 is {0}".format(1+2))

class Default(dict):
	def __missing__(self, key):
		return key
print('{name} was born in {country}'.format_map(Default(name='Guido')))

print('hello'.islower())
print('hello'.isupper())
print(','.join('AEIOU'))
print('SAIFULLAH'.lower())
print('HELLO_SIR'.partition('_'))
print('I had A toy thAt wAs very expensive!'.replace('A','a'))
a = 'saif    '
print(a,len(a.rstrip()))

print('i-can-work-for-you'.split('-'))
print('i\ncan\nwork\nfor\nyou'.splitlines())
a = '     hello    '
print(a.strip())
print('From- emai'.startswith('From-'))
print('AbCdE'.swapcase())
print('the new era of knowledge'.title())
