def printstack(stack,maxx):
    global pd
    global name
    for i in range (maxx+1):
        print(pd[stack[i]],end=' ')
    print()

def pick (stack,Index_Stack,money,Index_product):
    global size_product
    global pd
    if Index_product < size_product:
        price= pd[Index_product]
        if money < price:
            pick (stack,Index_Stack,money,Index_product+1)#check product more
        else:
            money-= price
            stack[Index_Stack]=Index_product
            if money ==0:
                printstack(stack,Index_Stack)
            else:
                pick (stack,Index_Stack+1,money,Index_product+1)
            pick(stack,Index_Stack,money+price,Index_product+1)


pd = [20, 10, 5, 5, 3, 2, 20, 10]
name = ['soap', 'potato chips', 'loly pop', 'toffy', 'pencil', 'rubber', 'milk','cookie'] 
M=20
size_product=len(pd)
stack=size_product*[-1]
Index_Stack=0
Index_product=0
pick(stack,Index_Stack,M,Index_product)



