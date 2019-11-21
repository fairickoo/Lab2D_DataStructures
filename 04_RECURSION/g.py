def move(n,A,C,B):
    print('def------------------->',n,A,C,B)
    if n==1:
        print('------------------>n==1')
        print (n,' ',A,C)
    else:
        print('------------------->n>1\n')
        print('move1     ',n,A,C)
        move(n-1,A,B,C) 
        
        print(n,' ',A,C,'\n')

        print('move2     ',n,A,C)
        move(n-1,B,C,A)

move(3,'A','C','B')  