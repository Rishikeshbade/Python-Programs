import math

def quadratic(a, b, c):
    delta = b * b - 4 * a * c

    if delta < 0:
        print("The roots are complex.")
        return None, None
    else:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        return root1, root2

a = float(input("Enter the value of coefficient a: "))
b = float(input("Enter the value of coefficient b: "))
c = float(input("Enter the value of coefficient c: "))

root1, root2 = quadratic(a, b, c)

if root1 is not None and root2 is not None:
    print("Root 1 of x:", root1)
    print("Root 2 of x:", root2)
