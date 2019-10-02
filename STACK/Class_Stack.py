class stack:
    def __init__(self,list=None):
        if list==None:
            self.items=[]
        else:
            self.items=list
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

