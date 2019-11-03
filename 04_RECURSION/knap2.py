

def printtemp(temp,maxx):
    global name
    global pd
    for i in range(maxx+1):
        print(pd[temp[i]],name[temp[i]],end=' ')
    print()

def pick(temp,i_t,money,i_pd):
    global pd
    global size_pd
    if i_pd < size_pd:
        price= pd[i_pd]
        if money< price:
            pick(temp,i_t,money,i_pd+1)
        else:
            money-=price
            temp[i_t]=i_pd
            if money==0:
                printtemp(temp,i_t)
            else:
                 pick(temp,i_t+1,money,i_pd+1)
            pick(temp,i_t,money+price,i_pd+1)
pd=[10,5,5,3,2,5,10]
name=['A','B','C','D','E','F','G']
money=10
size_pd=len(pd)
temp=size_pd*[-1]
i_pd=0
i_t=0
pick(temp,i_t,money,i_pd)
