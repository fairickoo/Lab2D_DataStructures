class node:
    def __init__(self,data,next=None):
        if next==None:
            self.next=None
        else:
            self.next=next
        self.data=data
    def __str__(self):
        return str(self.data)
    def getData(self):
        return self.data
    def getNext (self):
        return self.next
    def setData(self,data=None):
        self.data=data
    def setNext(self,next=None):
        self.next=next

