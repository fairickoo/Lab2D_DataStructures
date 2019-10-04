from Class_Node import node

class List:
    def __init__(self,head=None):
       self.head=head
       self.count=0
    def __str__(self):
        if self.head==None:
            return 'None'
        else:
            out=''
            cur=self.head
            self.count=1
            while cur.next!=None:
                self.count+=1
                out+= str(cur.data) +' '
                cur=cur.next
            out+= str(cur.data)
            return str(out )

    def append(self,data):
        if self.head==None:
            self.head=data
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=data
    def size(self):
        return self.count
    def isEmpty(self):
        return self.head==None
    def addHead(self,data):
        newHead=data
        newHead.next=self.head
        self.head=newHead
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
            newTail.next=None
    def isIn(self,data):
        if self.head==None:
            self.head=data
        else:
            check=data
            cur=self.head
            while cur.next!=None:
                if cur.data==check:
                    return True
                else:
                    cur=cur.next  
            if cur.data==check:
                return True
            else:
                return False 
    def before(self,data):
        if self.head==None or not self.isIn(data):
            return str(data)+' no list'
        else:
            cur=self.head
            while cur.next!=None:
                if cur.next.data==data:
                    break
                cur=cur.next
            return 'before '+str(data)+' is '+str(cur)
    def remove(self,data):
        if self.head==None or  self.isIn(data)==False:
            return str(data)+' no list'
        else:
            removeN=None
            cur=self.head
            while cur.next!=None:
                if cur.next.data==data:
                    break
                cur=cur.next
            removeN=cur.next
            cur.setNext(removeN.next)
            removeN.setNext(None)
        return removeN    #-->B
    def removeTail (self):
        if self.head==None :
            return 'no list for delete'
        else:
            removeN=None
            cur=self.head
            while cur.next.next!=None:
                cur=cur.next
            removeN=cur.next
            cur.setNext(None)
        return removeN
    def removeHead (self):
        if self.head==None :
            return 'no list for delete'
        else:
            removeN=None
            removeN=self.head
            self.head=removeN.next
            removeN.setNext(None)
        return removeN
    def addIndex (self,index,data):
        addN=data
        if index==0:
            self.addHead(data)
        else:
            cur=self.head
            cur_index=0
            while cur.next!=None:
                if cur_index==(index-1):
                    addN.next=cur.next
                    cur.next=addN
                cur=cur.next
                cur_index+=1
            if cur_index==(index-1):
                self.addTail(data)
                data.setNext(None)
    def removeIndex(self,index):
        removeN=None
        if index==0:
            self.removeHead()
        else:
            cur=self.head
            cur_index=0
            while cur.next!=None:
                if cur_index==(index-1):
                    removeN=cur.next
                    cur.setNext(removeN.next)
                    removeN.setNext(None)
                cur=cur.next
                cur_index+=1
            if cur_index==(index-1):
                removeN=cur.next
                cur.setNext(removeN.next)
                removeN.setNext(None)
            return removeN
            




            





