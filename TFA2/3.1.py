firstname = input ('Enter your first name: ')
lastname = input ('Enter your last name: ')
age = input ('Enter your age: ')

print ('==============================================================')
print ('Full Name: ', firstname, lastname)

sliced_name = firstname [0:4]
print ('Sliced Name: ', sliced_name)

greeting_message = 'Greeting Message: Hello, {}! Welcome. You are {} years old.'
print (greeting_message.format(sliced_name, age))