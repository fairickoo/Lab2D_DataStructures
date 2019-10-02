from Class_Stack import stack

def match(pp,cc):
    if (pp=='{'and cc=='}')or(pp=='('and cc==')')or(pp=='['and cc==']'):
        return True
    else:
        return False

st1='( a+b-c *[d+e]/{f*(g+h) }'
st2='[ ( a+b-c }*[d+e]/{f*(g+h) }'
st3='( 3 + 2 ) / { 4**5 }'
st4='456'
s=stack()
error= False
for x in st3:
    if x=='{'or x=='[' or x=='(':
        s.push(x)
    elif x=='}'or x==']' or x==')':
        if  s.isEmpty()==True:
            error=True
        else:
            open=s.pop()
            if match(open,x)==False:
                error=True
                
if error:
    print('MISMATH')
elif s.isEmpty()==False:
    print('MISMATCH open paren. exceed')
else :
    print('MATCh')
