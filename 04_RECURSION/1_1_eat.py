def eat(n):
    if n==1:
        print('eat',n)
    else:
        eat(n-1)
        print(' eatt',n,end='')
        
eat(5)