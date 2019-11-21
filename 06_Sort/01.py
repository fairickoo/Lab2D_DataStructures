from math import log2
from math import floor

def insertMinHeap(lists,i):
    print('insert',lists[i],'at index',i,end='    ')
    print(lists)
    insertEle=lists[i]  
    fi=(i-1)//2
    print('fi : ',fi)
    while i >0 and insertEle < lists[fi]:
        lists[i]=lists[fi]
        i=fi
        fi=(i-1)//2
    lists[i] = insertEle

def print90(h, i, max_i):
    if i <= max_i:
        indent = floor(log2(i+1))
        print90(h, (i*2)+2, max_i)
        print('    ' * indent, h[i])
        print90(h, (i*2)+1, max_i)

def deleteMin(h, last):
    print('delMin', h[0], 'last index = ', last, end='     ')
    print(h)
    insertEle = h[last]
    h[last] = h[0]
    hole = 0
    ls = hole*2 + 1
    found = False
    while ls < last and not found:
        rs = ls if ls+1 >= last else ls+1
        min = ls if h[ls] < h[rs] else rs  # minson index
        if h[min] < insertEle:
            h[hole] = h[min]  # promote small son up to hole
            hole = min  # going down the tree
            ls = hole*2+1
        else:
            found = True
    h[hole] = insertEle

h = [89, 85, 97, 5, 200,300,400]
sort=[]
for i in range(1, len(h)):
    print(h)
    print90(h, 0, i)
    insertMinHeap(h, i)
    print('------------------\n')
      
for last in range(len(h)-1, -1, -1):
    sort.append(h[0])
    deleteMin(h, last)
    print(h)
    print90(h, 0, last)
    print('------------------\n')
 

print("===========sorting a ============")
print(sort)
print()