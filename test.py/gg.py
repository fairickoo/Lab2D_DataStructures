def height(root):
    if root==None:
        return -1
    else:
        hl=height(root.left)
        hr=height(root.right)
        if hl>hr:
            return hl+1
        else:
            return hl+1
def depth(root,data):
    if root.data==data:
        return 0
    if root ==None:
        return -1
    else:
        if data< root.data:
            return -- 
        elif
            return---

def father (root,data):
    if search(root.data)!=None:
        if _father(root,data)!=None:
            print('real')
        else:
            print('root')
    else:
        print('nolist')
def _father(root,data):
    if root.data==data:
        return None
    if root.right!=None:
        if root.right.data==data:
            return root
    elif root.left!=None:
        if root.left.data==data:
            return root
    if root!=None:
        if data
            return 
        else:
            return 