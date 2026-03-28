def add(a,b):
  return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
       print("division by zero")
       return 0
    else:
        return a/b
a=int(input("Enter a number"))
b=int(input("Enter another number"))
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
ch=int(input("Enter your choice"))
if ch==1:
    print(add(a,b))
elif ch==2:
    print(mul(a,b))
elif ch==3:
    print(mul(a,b))
elif ch==4:
    print(div(a,b))
else:
    print("Please enter a valid choice")
