def fac(n):
    if n==1 or n==0:
        return 1
    else:
        return fac(n-1)*n
def sum1ToN(n):
    if n==0:
        return 0
    elif n==1:
        return n
    else:
        return sum1ToN(n-1)+n

def printNTo1(n):
    if n>0:
        print(n,end=' ')
        printNTo1(n-1)

def print1ToN (n):
    if n>0:
        print1ToN(n-1)
        print(n,end=' ')

def fib (n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)




print('fac :' ,fac(1))
print('sum1ToN :' ,sum1ToN(2))
printNTo1(5)
print('\n')
print1ToN(5)
print('\nfibonaci ',fib(4))