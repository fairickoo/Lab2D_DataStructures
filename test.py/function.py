def binarysearch(fromL,toL,x,lists):
    mid=(fromL+toL) //2
    if fromL>toL:
        return 'None'
    if x==lists[mid]:
        return mid
    elif x>lists[mid]:
        return binarysearch(mid+1,toL,x,lists)
    else:
        return binarysearch(fromL,mid-1,x,lists)
def move (n,A,C,B):
    if n==1:
        print(n,' ',A,C)
    else:
        move (n-1,A,B,C)
        print(n,' ',A,C)
        move(n-1,B,C,A)

def sum1Nto1_n(n,lists):
    if n==1:
        return lists[0]
    else:
        x=sum1Nto1_n(n-1,lists)
        y=lists[n-1]
        return x+y
def sumfrom(fromL,toL,lists):
    if fromL>toL:
        return 'None'
    if fromL==toL:
        return lists[fromL]
    else:
        x=sumfrom(fromL+1,toL,lists)
        y=lists[fromL]
        return x+y
def sumNo_n (lists):
    n=len(lists)
    if n==1:
        return lists[0]
    else:
        x=sumNo_n (lists[1:])
        y=lists[0]
        return x+y
def printlistsF(n,lists):
    if n==1:
        print(lists[0],end=' ')
    else:
        printlistsF(n-1,lists)
        print(lists[n-1],end=' ')
def printlistsB(n,lists):
    if n==1:
        print(lists[0],end=' ')
    else:
        print(lists[n-1],end=' ')
        printlistsB(n-1,lists)
def printlistsF_n(lists):
    n=len(lists)
    if n==1:
        print(lists[0],end=' ')
    else:
        print(lists[0],end=' ')
        printlistsF_n(lists[1:])
def appF(lists,items):
    if items==1:
        lists.append(items)
    else:
        appF(lists,items-1)
        lists.append(items)
def appB(lists,items):
    if items==1:
        lists.append(items)
    else:
        lists.append(items)
        appB(lists,items-1)
class node:
    def __init__(self,data,next=None):
        self.data=data
        if next==None:
            self.next=None
        else:
            self.next=next

def printLists(items):
    if items!=None:
        print(items.data,end=' ')
        printLists(items.next)
        


        


        

    
li=[2,6,7,12,19,20,23]
print(binarysearch(0,5,23,li))

move (3,'A','C','B')

li2=[1,2,3]
print(sum1Nto1_n(len(li2),li2))
print(sumfrom(0,3,li))
print(sumNo_n (li2))
printlistsF(len(li2),li2)
print()
printlistsB(len(li2),li2)
print()
printlistsF_n(li2)
l=[]
appF(l,5)
print(l)
print()
appB(l,5)
print(l)
print()
n2=node('C')
n1=node('B',n2)
n=node('A',n1)
printLists(n)