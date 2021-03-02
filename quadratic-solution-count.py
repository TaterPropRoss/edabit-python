'''
A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct solutions for real values of x. Given a, b and c, you should return the number of solutions to the equation.

Examples
solutions(1, 0, -1) ➞ 2
// x² - 1 = 0 has two solutions (x = 1 and x = -1).

solutions(1, 0, 0) ➞ 1
// x² = 0 has one solution (x = 0).

solutions(1, 0, 1) ➞ 0
// x² + 1 = 0 has no real solutions.
Notes
You do not have to calculate the solutions, just return how many there are.
a will always be non-zero.
'''

def solutions(a,b,c):
    # basic checks:
    if a == 0: 
        return 0
    # QF: x1 = (-b [+/-] math.sqrt(b^2 -4*a*c)) / 2 * a
    # so the number of solutions is determined by the b^2 -4ac term   
    # print("A: %2d, B: %2d, C: %2d" %(a,b,c))
    rootNumber =  ((b*b) - (4*a*c))
    if rootNumber < 0:
        return 0
    elif rootNumber == 0:
        return 1
    elif rootNumber > 0:
        return 2
# see how many solutions there are at ax^2 + bx + c = 0 

print(solutions(1, 0, -1))
print(solutions(1, 0, 0))
print(solutions(1,0,1))