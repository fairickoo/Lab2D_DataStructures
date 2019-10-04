from Class_Stack import stack


#input_infix=str(input("Enter infix expression"))
st1='a+b*c-d'
st2='a+b*c-(d/e+f)*g'
st3='(a+b)*c/d'
st4='+*-(/+)*'
s=stack()
p=stack()
state=0
out=''
n=1
for x in st3:
    s.push(x)

for x in range(s.__len__()):
    
    if (s.items[x]>='a' and s.items[x]<='z'):
            out+=s.items[x]
    elif (s.items[x]=='+' or s.items[x]=='-' or s.items[x]=='*' or s.items[x]=='/' ):
                if p.isEmpty():
                    p.push(s.items[x])
                    print('head :',p)
                else:
                        if  (str(p.items[0])=='+' or str(p.items[0])=='-') and (s.items[x]=='*' or s.items[x]=='/' ):
                            p.push(s.items[x])
                            print(p)
                        elif (str(p.items[0])=='+' or str(p.items[0])=='-') and(s.items[x]=='+' or s.items[x]=='-') :
                            xpop=p.pop()
                            x1pop=p.pop()
                            p.push(s.items[x])
                            print('pop-->',xpop)
                            print('pop-->',x1pop)
                            out+=xpop+x1pop
                            print(p)
                
                        
    
        
            
            
            
out+=str(p)
                    


print('out ',out)