class node:
    def __init__(self,data,right=None,left=None):
        self.data=data
        self.right=None if right==None else right
        self.left=None if left==None else left
    def __str__(self):
        return str(self.data)

def addi(root,data):
    if root==None:
        return node(data)
    else:
        if data< root.data:
            root.left=addi(root.left,data)
        else:
            root.right=addi(root.right,data)
        return root
def printSideway(root,level):
    if root != None:
        printSideway(root.right,level+1)
        print('   '*level,root.data)
        printSideway(root.left,level+1)
def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root,end=' ')
        inOrder(root.right)
def preOrder(root):
    if root != None :
        print(root,end=' ')
        preOrder(root.left)
        preOrder(root.right)
def postOrder(root):
    if root != None :
        postOrder(root.left)
        postOrder(root.right)
        print(root,end=' ')
def path (root,data):
    if search(root,data)!=None:
        if root ==None or root.data==data:
            return root
        if data > root.data:
            print(root,end=' ')
            return path(root.right,data)
        else:
            print(root,end=' ')

            return path(root.left,data)
        return root
    else:
        print('No data not found')
def search(root,data):
    if root==None or root.data==data:
        return root
    if data > root.data:
        return search(root.right,data)
    else:
        return search(root.left,data)
#---------------------------------------------
def height(root):
    if root == None:
        return -1
    else:
        hL=height(root.left)  
        hR=height(root.right)  
        #print('hr :',hR)
        if hL>hR:
            return hL+1
        else:
            return hR+1  
def depth(root,data):
    if search (root,data)!=None:
        if root ==None :
            return -1
        if root.data==data:
            return 0
        else:
            if data < root.data:
                return depth(root.left,data)+1
            elif data > root.data:
                return depth(root.right,data)+1
    else:
        print('No data for depth')
            
def smallest(root):
    if root.left ==None:
        return root
    else:
        return smallest(root.left)
def father(root,data):
    if search(root,data)!= None:
        f=_father(root,data)
        if  f!= None:
           print('father of', data, 'is',f)
        else:
             print('father of', data, 'is', f, data, 'is root') 
    else:
        print("No data", data)
        return 

def _father (root,data):
    if root.data==data:
        return None
    if root.right!=None:
        if root.right.data==data:
            return root
    elif root.left != None:
        if root.left.data==data:
            return root
    if root != None:
        if data < root.data:
            return _father(root.left,data)
        else:
            return _father(root.right,data)

#-------------------------------------------------

li =[14,4,9,7,15,3,18,16,20,5,16]
r=None
for i in li:
    r= addi(r,i)
print(r)
print('\n sideway')
printSideway(r,0) 

print('\ninorder  :',end='')  
inOrder(r) 

print('\npreorder  :',end='')  
preOrder(r) 
print('\npostorder  :',end='')  
postOrder(r) 

d = 19
print('path:', d, '=', end = ' ')
path(r, d)
print()
d = 9
t = search(r, d)
print('search ',d,' : ',t.data)

print('\nheight of ', r.data, '=', height(r))
d = 20
print('depth of node data ', d, '=', depth(r, d))

print('smallest data = ', end='')
print(smallest(r))


dfather = 7
father(r, dfather)


