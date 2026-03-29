def sumdigit(n):
    if n==0:
        return 0
    else:
        return (n%10)+sumdigit(n//10)
num=int(input("Enter n:"))
print("Sum of digit:",sumdigit(num))



