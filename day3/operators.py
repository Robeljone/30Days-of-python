# #Day three of 30days
# from math import pi
# age = 25
# p_height = 1.70
# comp_num = complex
# base = input('Enter Base: ')
# height = input('Enter Height: ')
# area = int(base)*int(height)
# print('he area of the triangle is: ',area)

# sideA = input('Enter Side A: ')
# sideB = input('Enter Side B: ')
# sideC = input('Enter Side C: ')
# perimeter = int(sideA)+ int(sideB) + int(sideC)
# print('The perimeter of the triangle is: ',perimeter)

# lengeth = input('Enter Length: ')
# width = input('Enter Width: ')
# area_rec = int(lengeth)+int(width)
# perimeter_rec = 2*(int(lengeth)+int(width))

# print('Area of a rectangle: ',area_rec)
# print('Perimeter of a rectangle',perimeter_rec)

# radius = input('Enter radius of a circle')
# area_cir = pi * int(radius)*int(radius)
# circumference = 2*pi*int(radius)

# print('Area of a circle is',area_cir)
# print('circumference of a circle is',circumference)

# x_inte = input('Enter X intersecpt')
# y_inte = 2*int(x_inte) - 2

# slot_x1 = input('Enter Slot X1: ')
# slot_y1 = input('Enter Slot Y1: ')
# slot_x2 = input('Enter Slot X2: ')
# slot_y2 = input('Enter Slot Y2: ')
# m = int(slot_y2)-int(slot_y1)/int(slot_x2)-int(slot_x1)

# print('Slope is: ',m)

# if m>y_inte:
#     print('Q#9 is greate')
# else:
#     print('Q#8 is greater')

# x_val = input('Enter the value of x')
# y_val = int(x_val)**2+6*int(x_val)+9

# print('The value of Y is: ',y_val)

# if 'python'=='python':
#     print('Equal Length')
# else:
#     print('Not Equal')

import string


print('on' in 'Python')
print('on' in 'Dragon')

leng = len('Python')
floa = float(leng)
stin = str(floa)
print(floa)
print(stin)

is_ev = input('Please enter Number')
if int(is_ev)%2 == 0:
    print('The Number is Even')
else:
    print('The Number is not even')

con_val = int(2.7)
if 7//3 == con_val:
    print('True')
else:
    print('False')

num_1 = '10'
num_2 = 10
if type(num_1) == type(num_2):
    print('True')

if '98' == 10:
    print('True')

hour = input('Enter Working Hour')
pay_per = input('Enter amount per Hour')

total_pay = int(hour) * int(pay_per)
print('Total salary is: ',total_pay)

year_lived = int(input('Enter years here'))
total_sec =int(year_lived)*(365*24*60*60)
print('Total seconds is: ',total_sec)
