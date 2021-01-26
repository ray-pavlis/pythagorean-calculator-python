from math import sqrt

print(
    'Pythagorean Calculator. Calculate the hypotenuse (side c) based on sides a and b.'
)

side_a = int(input('Input the length of side a: '))
side_b = int(input('Input the length of side b: '))

side_c = sqrt(side_a * side_a + side_b * side_b)
total = round(side_c,2)

print('The length of side c is: ')
print(total)
