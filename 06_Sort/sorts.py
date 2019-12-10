def Buble_sort (lists):
    n=len(lists)
    for x in range (n):
        for y in range (n) :
            if lists[x]< lists[y]:
                temp=lists[x]
                lists[x]=lists[y]
                lists[y]=temp
    print(lists)

def Straight_Selection_Sort  (a) :
    n=len (a)
    
    for i in range(n-1,-1,-1):
        big=a[0]
        ia=0
        for j in range(1,i):
            if a[j]>big:
                big=a[j]
                ia=j
        a[i],a[ia]=a[ia],a[i]
    print(a)

def insert (a):
    n=len(a)
    for i in range(n):
        ist=a[i]
        for j in range(i,-1,-1):
            if ist<a[j-1] and j>0:
                a[j]=a[j-1]
                print(a)
            else:
                a[j]=ist
                print(a)
                break
    print(a)

def shell(l, dIncrements):
    for inc in dIncrements: #for each deminishing increment
        for i in range(inc,len(l)): #insertion sort
            iEle = l[i] #inserting element
            for j in range(i, -1, -inc):
                if iEle<l[j-inc] and j >= inc:
                    l[j] = l[j-inc]
                else:
                    l[j] = iEle
                    break
    print(l)

               



#l=[4,3,9,4,5]
#Buble_sort (l)
#Straight_Selection_Sort (l)
#insert (l)
l = [10,11,1,13,2,6,4,12,5,8,7,9,3]
dIncrements = [5,3,1]
shell(l, dIncrements)
