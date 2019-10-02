from Class_List import List
from Class_Node import node
import math

def BottomUp(value,word):
    for x in range(value):
        word.append(word.removeHead())

def Riffle(value,word):
    check_value = word.size() - value
    if value < check_value:
        insert=1
        for x in range (value,9):
            word.addIndex(insert,word.removeIndex(x))
            insert+=2    
            if check_value==6 and x==7:
                break
            elif check_value==7 and x==5:
                break
            elif check_value==8 and x==3:
                break
            elif check_value==9 and x==1:
                break   
    else:
        insert=1
        if check_value==value:
            for x in range (value,9):
                word.addIndex(insert,word.removeIndex(x))
                insert+=2
        elif value>check_value:
            insert=1
            for x in range (value,9):
                word.addIndex(insert,word.removeIndex(x))
                insert+=2
            word.addIndex(insert,word.removeTail())
        
def DeRiffle(value,word):
    check_value = word.size() - value
    if check_value >value:
        for x in range(1,value,1):
            word.addIndex(value,word.removeIndex(x))
    else:
        for x in range(1,check_value+1,1):
            word.append(word.removeIndex(x))

def DeBotton(value,word):
    for x  in range(value):
        word.addHead(word.removeTail())
        
        








ls=List()

for x in range(1,11):
    ls.append(node(x))
print('original word        : ',ls)

input_BottomUp=int(math.ceil(int(input('Enter percent for BottomUp :'))/10))
BottomUp(input_BottomUp,ls)
print('BottomUp word        : ',ls)

input_Riffle=int(math.ceil(int(input('Enter percent for Riffle :'))/10))
Riffle(input_Riffle,ls)
print('Riffle word          : ',ls)

DeRiffle(input_Riffle,ls)
print('DeRiffle update      : ',ls)

DeBotton(input_BottomUp,ls)
print('DeBotton update      : ',ls)