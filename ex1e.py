def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter a number"))
for i in range(n):
    print(fibonacci(i))
[25bcs147@mepcolinux ex4]$cat ex4e.py
def sunion(s1, s2):
    return s1 | s2
def sintersection(s1, s2):
    return s1 & s2
def sdifference(s1, s2):
    return s1 - s2
def ssubtract(s1, s2):
    return s1 - s2
def ssymmetric_difference(s1, s2):
    return s1 ^ s2
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Union:", sunion(a, b))
print("Intersection:", sintersection(a, b))
print("Difference (a - b):", sdifference(a, b))
print("Subtract (a - b):", ssubtract(a, b))
print("Symmetric Difference:", ssymmetric_difference(a, b))
