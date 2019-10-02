from Class_Node import node
class List :
    def __init__(self,head=None):
        self.head=head
        self.count=0
    def __str__(self):
        if self.head==None:
            return 'Head reference None'
        else:
            out=''
            cur=self.head
            self.count=1
            while cur.next!=None:
                out+= str(cur.data)+' '
                self.count+=1
                cur=cur.next
            out+= str(cur.data)+' '
            return out
            
    def append (self,data):
        if self.head==None:
            self.head=data
        else:
            cur=cur.next
            while cur.next!=None:
                cur=cur.next
            cur.next=data

    def size(self):
        return self.count
    
    def isEmpty(self):
        return self.head==None

    def addHead(self,data):
        newData=data
        if self.head==None:
            self.head=data
        else:
            newData.next=self.head
            self.head=newData
    def isIn(self,data):
        check=data
        if self.head==None:
            return 'No data'
        else:
            cur=self.head
            while cur.next!=None:
                if cur.data==check.data:
                    return True
                cur=cur.next
            if cur.data==check.data:
                return True
            else:
                return False
    def before (self,data):
        if self.head==None or self.isIn==False:
            return 'No data'
        else:
            check=data
            cur=self.head
            while cur.next!=None:
                if cur.next.data==check.data:
                    break
                cur=cur.next
            return 'before '+str(data)+' is '+str(cur)
    def remove (self,data):
        if self.head==None or self.isIn==False:
            return 'No data for remove'
        else:
            check=data
            removeN=None
            cur=self.head
            while cur.next!=None:
                if cur.next.data==check.data:
                    break
                cur=cur.next
            removeN=cur.next
            cur.setNext(removeN.next)
            removeN.setNext(None)
        return removeN
    def removeHead(self):
        removeH=None
        if self.head==None or self.isIn==False:
            return 'No data for remove'
        else:
            removeH=self.head
            self.head=removeH.next
            removeH.setNext(None)
    def removeTail(self):
        if self.head==None or self.isIn==False:
            return 'No data for remove'
        else:
            removeT=None
            cur=self.head
            while cur.next.next!=None:
                cur=cur.next
            removeT=cur.next
            cur.setNext(None)
    
    def addIndex(self,index,data):
        if index==0:
            self.addHead(data)
        else:
            newN=data
            cur_index=0
            cur=self.head
            while cur.next!=None:
                if cur_index==(index-1):
                    newN.next=cur.next
                    cur.next=newN
                cur=cur.next
                cur_index+=1
            
            self.addTail(data)
            data.setNext(None)
    def addTail(self,data):
        if self.head==None :
            return 'no list for delete'
        else:
            newTail=data
            cur=self.head
            while cur.next.next!=None:
                cur=cur.next
            newTail.next=cur.next
            cur.next=newTail







            





n5=node('E')
n4=node('D',n5)
n3=node('C',n4)
n2=node('B',n3)
n1=node('A',n2)

ls=List()
print('isEmpty :',ls.isEmpty())
ls.append(n1)
print('original list : ',ls)
print('original size : ',ls.size())
print('isEmpty :',ls.isEmpty())

m=node('R')
ls.addHead(m)
print('update list : ',ls)
print('update size : ',ls.size())
m1=node('W')
m2=node('B')
print(ls.isIn(m1))
print(ls.isIn(m2))
mm=node('R')
print(ls.before(mm))

mm1=node('D')
print(ls.remove(mm1))
print('update list : ',ls)
print('update size : ',ls.size())
ls.removeHead()
print('update list : ',ls)
print('update size : ',ls.size())
ls.removeTail()
print('update list : ',ls)
print('update size : ',ls.size())
mm12=node('W')
ls.addIndex(2,mm12)
print('update list : ',ls)
print('update size : ',ls.size())