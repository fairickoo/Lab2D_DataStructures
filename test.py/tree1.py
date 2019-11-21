class node :
    def __init__(self,data,right=None,left=None):
        self.data=data
        self.right=None if right==None else right
        self.left=None if left==None else left
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self,root=None):
        self.root=None if root==None else root
    def add(self,data):
        self.root=BST._add(self.root,data)
    def _add(root,data):
        if root==None:
            return node(data)
        else:
            if data < root.data:
                root.left= BST._add(root.left,data) 
            else:
                root.right=BST._add(root.right,data)
        return root
    def printsideway(self):
        BST._printsideway(self.root,0)
    def _printsideway(root,level):
        if root!=None:
            BST._printsideway(root.right,level+1)
            print('   '*level,root.data)
            BST._printsideway(root.left,level+1)
            
    def search(self,data):
        return BST._search(self.root,data)
    def _search(root,data):
        if root==None or root.data==data:
            return root
        if data < root.data:
            return BST._search(root.left,data)
        else:
            return BST._search(root.right,data)
    
    def path(self,data):
        BST._path(self.root,data)
    def _path(root,data):
        if root ==None:
            return root
        if data< root.data:
            print(root,end=' ')
            return BST._path(root.left,data)
        else:
            print(root,end=' ')
            return BST._path(root.right,data)
    def delete(self,data):
        BST._delete(self.root,data)
    def _delete(root,data):
        if root==None:
            return root
        if data > root.data:
            root.right= BST._delete(root.right,data)
        elif data < root.data:
            root.left= BST._delete(root.left,data)
        else:
            if root.right==None:# case one child 
                return root.left
            elif root.left ==None: 
                return root.right
            else:
                temp=BST.findmin_N(root.right)
                root.data=temp.data
                root.right=BST._delete(root.right,temp.data)
        return root
    def findmin_N(root):
        if root.left ==None:
            return root
        else:
            return BST.findmin_N (root.left)
def father(root,data):
        if BST.search(root,data)!=None:
            if _father(root,data)!= None:
                print('father of ',data,'is',_father(root,data))
            else:
                print('no father ',data,'is root')
        else:
            print('no data')
            return 
def _father(root,data):
    if root.data==data:
        return None
    if root.right !=None:
        if root.right.data==data:
            return root
    elif root.left!=None:
        if root.left.data==data:
            return root
    if root !=None:
        if data <root.data:
            return _father(root.left,data)
        else:
            return _father(root.right,data)
        
            


"""l = [int(e) for e in input("insert integers : ").split()]
print(l)"""

li=[14,4,9,7,15,3,18,16,20,5,16]
t=BST()
print(li)
for i in li:
    t.add(i)
print(t)
t.printsideway()
print()
print(t.search(13))
t.path(5)
print()
t.delete(4)
t.printsideway()
r=None
dfather = 20
father(r, dfather)