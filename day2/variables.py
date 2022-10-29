#Day 2: 30 Days of python programming
from math import pi
first_name = 'Robel'
last_name = 'Kidane'
full_name = first_name+last_name
country = 'Ethiopia'
city = 'Addis Ababa'
age = 25
year = 1997
is_married = 'Single'
is_true = True
is_light = False

profession,experince,tech = 'Full Stack dev',2,'React,Node js,Python'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))

print('The length of first name:',len(first_name))
len_first = len(first_name)
len_last = len(last_name)

if len_first>len_last:
   print('First Name is greater')
else:
   print('Second is greater')

num_one = 5
num_two = 4
total = num_one+num_two
dif = num_two - num_one
product = num_one*num_two
division= num_one/num_two
exp = num_one**num_two
floor_division = num_one//num_two

radius = input('Enter radius of a circle')
rad = int(radius)
area_of_circle = pi * rad**2
first_name = input('Enter first Name')
last_name = input('Enter last name')
country = input('Enter your Country')
age = input('Enter your age')



