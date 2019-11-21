def eat (n):
    if n==1:
        print(n,end=' ')
    else:
        eat(n-1)
        print(n, end=' ')

def eat1(n):
    if n==1:
        print(n,end= ' ')
    else:
        print(n,end=' ')
        eat1(n-1)
def fac (n):
    if n==0 or n==1:
        return 1 

    else:
        return fac(n-1)*n
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
def sum_1ToN (n):
    if n==1:
        return n
    else:
        return sum_1ToN(n-1)+n

def sum_lists_n_L (n,lists):
    if n==0:
        return 'None'
    elif n==1:
        return lists[0]
    else:
        x = sum_lists_n_L(n-1,lists)
        y = lists[n-1]
        return x+y

def sum_selectIndex (FromL,ToL,lists):
    if ToL<FromL:
        return 'None'
    elif ToL==FromL:
        return lists[FromL]
    else:
        x=sum_selectIndex (FromL+1,ToL,lists)
        y=lists[FromL]
        return x+y

def sum_subLists(lists):
    n= len(lists)
    if n==0:
        return 'None'
    elif n==1:
        return lists[0]
    else:
        x=sum_subLists(lists[1:])
        y=lists[0]
        return x+ y

def printNto1(n):
    if n==1:
        print(n,end=' ')
    else:
        print(n,end=' ')
        printNto1(n-1)
def print1toN(n):
    if n==1:
        print(n,end=' ')
    else:
        print1toN(n-1)
        print(n,end=' ')
def printListForw(n,lists):
    if n==0:
        return 'None'
    elif n==1:
        print(lists[0],end=' ')
    else:
        printListForw(n-1,lists)
        print(lists[n-1],end=' ')

def printListBkw(n,lists):
    if n==0:
        return 'None'
    elif n==1:
        print(lists[0],end=' ')
    else:
        print(lists[n-1],end=' ')
        printListBkw(n-1,lists)

def printListForw1(lists):
    n=len(lists)
    if n==0:
        return 'None'
    elif n==1:
        print(lists[0],end=' ')
    else:
        print(lists[0],end=' ')
        printListForw1(lists[1:])
        
def printListBkw1(lists):
    n=len(lists)
    if n==0:
        return 'None'
    elif n==1:
        print(lists[0],end=' ')
    else:
        printListBkw1(lists[1:])
        print(lists[0],end=' ')



def binarySearch(lo,hi,lists,s):
    mid = (lo+hi)//2
    if lo>hi:
        return 'None'
    if s==lists[mid]:
        return mid
    elif s>lists[mid]:
            return binarySearch(mid+1,hi,lists,s) 
    else :
            return binarySearch(lo,mid-1,lists,s)
def move(n,A,C,B):
    if n==1:
        print (n,' ',A,C)
    else:
       move(n-1,A,B,C) 
       print(n,' ',A,C)
       move(n-1,B,C,A)

def appF(lists,items):
    if items==1:
        lists.append(1)
    else:
        appF(lists,items-1)
        lists.append(items)

def appB(lists,items):
    if items==1:
        lists.append(1)
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

    
def createLLL(head,n):
    global fromList
    if n>=0:
        last=node(fromList[n],head)
        p=createLLL(last,n-1)
        return p
    else:
        return head

def createLL(head, lists): 
    if lists != []:
        p = node(lists[-1], head)
        p = createLL(p, lists[:-1])
        return p
    else:
        return head


print('eat 1 to N  :  ',end= ' ')
eat(5)

print('\neat 1 to N  :  ',end= ' ')
eat1(5)

print('\nfac         :',end=' ')
print(fac(3))

print('\nfib         :',end=' ')
print(fib(7))

print('index search: ',end=' ')
lists=[1,3,4,5,17,18,31,33,35]
print(binarySearch(0,8,lists,33))

print('\n----move A to C -3----')
move(3,'A','C','B')  

print('\n----------SUM---------',end=' ')
print('\nsum_1toN     :',end=' ')
print(sum_1ToN(5))
print('sum_lists_n_L  :',end=' ')
l1=[1,2,3,1,2,3]
print(sum_lists_n_L(len(l1),l1))
print('sum_selectIndex:',end=' ')
print(sum_selectIndex (0,3,l1))
print('sum_subLists   :',end=' ')
print(sum_subLists (l1))
print('----------------------')

print('\n----------print--------',end=' ')
print('\nprint N to 1     :',end=' ')
printNto1(5)
print('\nprint 1 to N     :',end=' ')
print1toN(5)
print('\nprint Lists forW :',end=' ')
l2=[1,2,4,5,6,7]
printListForw(len(l2),l2)
print('\nprint Lists Bkw  :',end=' ')
printListBkw(len(l2),l2)
print('\nprint Lists Frow no n  :',end=' ')
printListForw1(l2)
print('\nprint Lists Bkw no n   :',end=' ')
printListBkw1(l2)
print('\n----------------------')

print('\n------append-------')
print('append 1 to N  :' ,end=' ')
st3=[]
appF(st3,5)
print(st3)
print('append N to 1  :' ,end=' ')
st4=[]
appB(st4,5)
print(st4)
print('\n------------------------') 

print('\n----print lits from node----')
n3=node('C')
n2=node('B',n3)
n1=node('A',n2)
printLists(n1)
print('\n----------------------------') 

print('\n---- createLLL1 -------' )
fromList = [2,5,4,8,6,7,3,1]
h = createLLL(None, len(fromList)-1) 
printLists(h)
print('\n-----------------------')

print('\n----- createLLL2 ------')
lists = [2,5,4,8,6,7,3,1]
h = createLL(None,lists)
printLists(h)
print('\n-----------------------')



