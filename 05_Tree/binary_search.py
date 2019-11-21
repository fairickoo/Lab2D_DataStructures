class node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left = None if left is None else left
        self.right = None if right is None else right

    def __str__(self):
        return str(self.data)
   
    def getData(self):
        return self.data
    def getRight(self):
        return self.data
    def getLeft(self):
        return self.left
    
    def setData(self,data):
        self.data=data
    def setRight(self,right):
        self.right=right
    def setLeft(self,left):
        self.left=left

class BST:
    def __init__(self,root=None):
        if root==None:
            self.root=None
        else:
            self.root=root
    def addI(self,data):# add ver2
        if self.root ==None:
            self.root=node(data)
        else:
            father=None
            cur=self.root
            while cur:
                father=cur
                if data < cur.data:
                    cur=cur.left
                else:
                    cur=cur.right

            if data < father.data:
                father.left = node(data)
            else:
                father.right = node(data)

    def add(self, data): #add ver2  14   : 14 4 9 7 15 3 18
        self.root = BST._add(self.root, data)

    def _add(root, data):#1=N-14 2=14-4 3=N-4 4=14-9 5=4-9 6=N-9 7=14-7 8=4-7 9=9-7 10=N-7 11=14-15 12=N-15
                        #13=14-3 14=4-3 15=N-3 16=14-18 17=15-18 18=N-18
        if root is None:
            return node(data)  #add 1=14 3=4 6=9 10=7 12=15 15=3 18=18
        else:
            if data < root.data:
                root.left = BST._add(root.left, data) #remem 2=4 4=9 7=7 9=7 13=3 14=3 
            else:
                root.right = BST._add(root.right, data)#remem 5=9 8=7 11=15 16=18 15=18
            return root
    def printSideway(self): #14   : 0
        BST._printSideway(self.root,0)
        print()
    def _printSideway(root,level): #1=14-0 2=15-1 3=N=2
        if root:  #not Non
            BST._printSideway(root.right,level+1)  #remem  1=15-1 2=N-2
            print('   '*level,root.data) #print  
            BST._printSideway(root.left, level+1)
    def inOrder(self):
        BST._inOrder(self.root) 
        
    def _inOrder(root):#14 4 3 9 7 5 15 18 16 16 20
        if root:
            #print('L :',root.left)
            BST._inOrder(root.left)# 4 3 N 7 5 N N 16 N N N
            print(root,end=' ') # print 3 N4 5 N7 N9 N14 15 16 N16 18 N20
            #print('R :',root.right)
            BST._inOrder(root.right)# N 9 N N N 15 18 16 N 20 N
    def preOrder(self):
        BST._preOrder(self.root)
    def _preOrder(root):
        if root:
            print(root,end=' ')
            BST._preOrder(root.left)
            BST._preOrder(root.right)
    def postOrder(self):
        BST._postOrder(self.root)
    def _postOrder(root):
        if root:
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root,end=' ')

    def search_Node (self,data): #14   :   16
        return BST._search_Node(self.root,data)
    def _search_Node(root,data):#1=14-16 2=15-16 3=18-16 4=16-16
        if root == None or root.data==data:
            return root #
        if data > root.data:
            return BST._search_Node(root.right,data) #1=15-16 2=18-16
        else:
            return BST._search_Node(root.left,data)# 3= 16

    def path (self,data):
        if self.search_Node(data)!=None:
            return BST._path(self.root,data)
        else:
            return 'No in lists'
    def _path(root,data):
        if root==None or root.data==data:
            #print(root,end=' ')
            return root
        if data> root.data:
            print(root,end=' ')
            return BST._path(root.right,data)
        else:
            print(root,end=' ')
            return BST._path(root.left,data)
        
    def delete_Node(self,data): #14  : 18
        BST._delete_Node(self.root,data)
    def _delete_Node(root,data):#1=14-18 2=15-18 3=20-18 4=20-20
        if root==None:
            return root
        if data>root.data:
            root.right= BST._delete_Node(root.right,data)# 1=15-18 2=20-18 
        elif data < root.data:
            root.left= BST._delete_Node(root.left,data)
        else:
            if root.right==None and root.left==None: #case no child
                return root==None
            elif root.right==None:# case one child 
                return root.left
            elif root.left ==None: 
                return root.right
            else:    #case two child
                temp = BST.findmin_node(root.right) 
                root.data = temp.data 
                root.right =BST._delete_Node(root.right,temp.data)
        return root
    def findmin_node(node):
        cur=node
        while (cur.left !=None):
            cur=cur.left
        return cur#20

        



li = [14,4,9,7,15,3,18,16,20,5,16]
t = BST()
for elem in li:
    t.add(elem)
print(li)

print('---inorder---')
t.inOrder()
print('\n-------------')

print('---preorder---')
t.preOrder()
print('\n-------------')

print('---postorder---')
t.postOrder()
print('\n-------------')

sd=5
print('---Search',sd,'---')
print(t.search_Node(sd))
print('-------------')

p=100
print('---path',p,'---')
print(t.path(p))
print('-------------')

print('---Sideway---')
t.printSideway()
print('\n-------------')

d=4
print('---delete',d,'---')
t.delete_Node(d)
print('---after delete---')
t.printSideway()
print('\n-------------')