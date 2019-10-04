from Class_List import List
from Class_Node import node
w=List()

n4=node('D')
n3=node('C',n4)
n2=node('B',n3)
n1=node('A',n2)

w.append(n1)
print('list : ',w)
n5=node('R')
w.addHead(n5)
print('\nadd R in Head : ',w)

print('\n isIn B :', w.isIn('B')) 
print(' isIn G :', w.isIn('G'))
print(' isIn D :', w.isIn('D'))
print(' isIn U :', w.isIn('U'))
print(' isIn Y :', w.isIn('Y'))
print(' isIn R :', w.isIn('R'))  
        
print(w.before('X'))
print(w.before('C'))

print('\nremove',w.remove('B'))
m=node('Z')
print(w.remove(m))
print('list update : ',w)

print('\nremoveTail',w.removeTail())
print('list update : ',w)

print('\nremoveHead',w.removeHead())
print('list update : ',w)
