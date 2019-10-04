from Class_Stack import stack

class Carpark:
    def __init__(self):
         self.car=stack()
    def arrive(self,i):
        if self.car.isFull():
            print('car',i,'cannot arrive : SOI FULL')
        else: 
            self.car.push(i)
            print ('car ',i,'arrive',end='     ')
            print('space left ',4-self.car.size())
    def depart(self,i):
        if i in self.car.items:
            temp=stack()
            print('car ',i,'depart:')
            for x in range(self.car.size(),-1,-1):
                if x!=i:
                    t=self.car.pop()
                    print('\tpop ',x,end='')
                    temp.push(t)
                else:
                    print('\tpop ',x,end='')
                    self.car.pop()
                    break
            
            space=4-self.car.size()
            for x in range(temp.size()-1,-1,-1):
                print('\tpush',temp.items[x],end='')
                self.car.push(temp.items[x])
            print('\n\tspace left ',space)   
            print('Soi = ',self.car.items)
           
        else:
            print('car',i,'cannot depart : No car',i)


    
c=Carpark()
for x in range(1,6):
    c.arrive(x)
print('Soi = ',c.car.items)

c.depart(7)
c.depart(2)