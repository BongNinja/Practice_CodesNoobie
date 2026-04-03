#factorial using Recursion
def Fac(a):
    if a!=0:
        k=a
        k=k*Fac(a-1)
    else:
        k=1
    return k
N =int(input("Enter the Number whose factorial you want to find out: \n"))
Fac(N)
print("the factorial of the number you specified is \n", Fac(N) )