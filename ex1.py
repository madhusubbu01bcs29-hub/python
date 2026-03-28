def isprime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def chechsum(num):
    for i in range(2,num):
        if isprime(i) and isprime(num-i):
            print(num,"=",i,"+",num-i)
            return
    print("not possible")
num=int(input("Enter a number"))
chechsum(num)
