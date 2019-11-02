class stack:
    def __init__(self,list=None):
        if list==None:
            self.items=[]
        else:
            self.items=list
    def __str__(self):
        out=''
        for x in self.items:
            out+=x
        return  str(out)
    def __len__(self):
        return len(self.items)
    def push (self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items==[]
    def peek (self):
        return self.items[-1]
    def isFull(self):
        if len(self.items)==4:
            return True
        else:
            return False
    def top(self):
        return self.items[0]


