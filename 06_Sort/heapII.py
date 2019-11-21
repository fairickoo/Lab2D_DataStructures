from math import log2
from math import floor

class node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data=None):
        self.data = data

    def setNext(self, next=None):
        self.next = next

class linkedlist:
    def __init__(self, head=None):
        self.head = head
    def __str__(self):
        if self.head==None:
            return 'this has no elements'
        else:
            out=''
            cur=self.head
            while cur.next!=None:
                out+= str(cur.data) +' '
                cur=cur.next
            out+= str(cur.data)
            return str(out )
    def size (self):
        if self.head ==None:
            return 'this has no elements'
        else:
            count=1
            cur=self.head
            while cur.next!=None:
                count+=1
                cur=cur.next
            return count
    def append(self,data):
        if self.head==None:
            self.head=data
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=data
    def foradd(self,i):
        cur=self.head
        for _ in  range(0,i):
            cur=cur.next
        return cur




def insertMinHeap(h,i):
    print('insert', h.foradd(i), 'at index', i, end = ' ')
    print('   ',h)
    insertEle=h.foradd(i).data
    fi=(i-1)//2
    while i > 0 and insertEle < h.foradd(fi).data:
        h.foradd(i).setData(h.foradd(fi).data)
        i=fi
        fi=(i-1)//2
    h.foradd(i).setData(insertEle)
def print90(h,i,max_i):
    if i<=max_i:
        indent=floor(log2(i+1))
        print90(h,(i*2)+2,max_i)
        print('   '*indent ,h.foradd(i))
        print90(h,(i*2)+1,max_i)

def deleteMin(h,last):
    print('delMin', h.foradd(0).data, 'last index = ', last, end = ' ')
    print('   ',h)
    insertEle= h.foradd(last).data
    h.foradd(last).setData(h.foradd(0).data)
    hole=0
    ls=hole*2+1
    found=False
    while ls < last and not found:
        rs = ls if ls+1 >= last else ls+1
        min = ls if h.foradd(ls).data < h.foradd(rs).data else rs  # minson index
        if h.foradd(min).data < insertEle:
            h.foradd(hole).setData(h.foradd(min).data)
            hole = min  # going down the tree
            ls = hole*2+1
        else:
            found = True
    h.foradd(hole).setData(insertEle)




    






n11=node(31)
n10=node(32,n11)
n9=node(26,n10)
n8=node(65,n9)            
n7=node(68,n8)
n6=node(19,n7)
n5=node(21,n6)
n4=node(24,n5)
n3=node(16,n4)
n2=node(12,n3)
n1=node(13,n2)
w=linkedlist()
w.append(n1)
print('list : ',w)

for i in range(1,w.size()):
    insertMinHeap(w,i)
    print('sort :',w)
    print90(w,0,i)
    print('-----------------')

for last in range(w.size()-1, -2, -1):
    deleteMin(w, last)
    print(w)
    print90(w, 0, last)
    print('------------------\n')

