"""
CHAPTER MODULARIZATION
In this program, I'll definite how to count area of triangle
"""
print('Count Area of Triangle with Data Skalar')
pad = 10
tall = 2
triangle = pad * tall / 2
print(f'Area of triangle with pad {pad}m and tall {tall}m is {triangle}m')

print('\nCount Area of Triangle with Repetition / Copy Paste')
pad = 50
tall = 4
triangle = pad * tall / 2
print(f'Second area of triangle with pad {pad}m and tall {tall}m is {triangle}m')

print('\nCount Area of Triangle with Function')
def count_triangle(pad, tall):
    triangle = pad * tall / 2
    return triangle

print(f'The area of triangle by function is {count_triangle(20, 3)}m')
print(f'The area of triangle by function is {count_triangle(15, 6)}m')