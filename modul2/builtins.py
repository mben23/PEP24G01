str1 = 'hello world'
print (type(str1))
int1 = 100
print (type(int1))
none = None
print (type(none))

result = str1.capitalize()
print ('Returned type:', type(result))


str1 = 'hello world {} {}'
result = str1.format('test' , 'test2')
print('Formated String:', result)

str1 = 'hello world'
result = str1.center(30, "#")
print(' Centered String:', result)

