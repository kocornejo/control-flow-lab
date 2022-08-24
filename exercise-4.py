# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:

a = input('length of triangle side a').lower()
b = input('length of triangle side b').lower()
c = input('length of triangle side c').lower()

# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length

if a == b and b == c:
    print(f'a triangle with sides {a}, {b} and {c} is an equalateral triangle')
elif a != b and a != c and b != c:
    print(f'a triangle with sides {a}, {b} and {c} is an scalene triangle')
else:
    print(f'a triangle with sides {a}, {b} and {c} is an isosceles triangle')
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle