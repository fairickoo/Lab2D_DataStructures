class node:
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
                root.left=BST._add(root.left,data)
            else:
                root.right=BST._add(root.right,data)
            return root
    def printSideway(self):
        BST._printSideway(self.root,0)
    def _printSideway(root,level):
        if root !=None:
            BST._printSideway(root.right,level+1)
            print('   '*level,root.data,)
            BST._printSideway(root.left,level+1)

    def inOrder(self):
        BST._inOrder(self.root)
    def _inOrder(root):
        if root != None:
            BST._inOrder(root.left)
            print(root,end=' ')
            BST._inOrder(root.right)

    def preOrder(self):
        BST._preOrder(self.root)
    def _preOrder(root):
        if root != None:
            print(root,end=' ')
            BST._preOrder(root.left)
            BST._preOrder(root.right)

    def postOrder(self):
        BST._postOrder(self.root)
    def _postOrder(root):
        if root != None:
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root,end=' ')
    
    def search_N (self,data):
        return BST._search_N(self.root,data)
    def _search_N(root,data):
        if root==None or root.data==data:
            return root
        if data< root.data:
            return BST._search_N(root.left,data)
        else:
            return BST._search_N(root.right,data)
    
    def path (self,data):
        if self.search_N(data)!=None:
            return BST._path(self.root,data)
        else:
            return 'no in list'
    def _path(root,data):
        if root==None or root.data==data:
            return root
        if data< root.data:
            print(root,end= ' ')
            return BST._path(root.left,data)
        else:
            print(root,end=' ')
            return BST._path(root.right,data)

    def delete_Node(self,data):
        BST._delete_Node(self.root,data)
    def _delete_Node(root,data):
        if root==None:
            return root
        if data>root.data:
            root.right= BST._delete_Node(root.right,data)
        elif data < root.data:
            root.left= BST._delete_Node(root.left,data)
        else:
            if root.right==None:# case one child 
                return root.left
            elif root.left ==None: 
                return root.right
            else:    #case two child
                temp = BST.findmin_node(root.right) 
                root.data = temp.data 
                root.right =BST._delete_Node(root.right,temp.data)
        return root
    def findmin_node(node):
        cur =node
        while cur.left !=None:
            cur=cur.left
        return cur

        

        

   
    


    

        



li = [12,5,7,3,9,5,6,1,2,20]
t=BST()
for i in li:
    t.add(i)
print(li)

t.printSideway()
t.inOrder()
print()
t.preOrder()
print()
t.postOrder()
print()
print(t.search_N(12))
print()
print(t.path(6))
t.delete_Node(7)
t.printSideway()