firstname = input ('Enter your first name: ')
lastname = input ('Enter your last name: ')
age = input ('Enter your age: ')
contact_num = input ('Enter contact number: ')
course = input ('Enter course: ')

output_text = "Last Name: {} \nFirst Name: {} \nAge: {} \nContact Number: {} \nCourse: {}"
f=open('TFA2/students.txt', 'a+')
f.write (output_text.format(lastname, firstname, age, contact_num, course))

line = f.readline ()
f.close ()

print ("\nStudent information has been saved to 'students.txt' file.")