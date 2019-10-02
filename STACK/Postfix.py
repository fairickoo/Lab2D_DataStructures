from Class_Stack import stack

def Postfix(word):
    p=stack()
    for x in word:
        if x>='0' and x<='9':
            p.push(ord(x)-48)
        elif x=='+':
            num1=p.pop()
            num2=p.pop()
            sum1=num2+num1
            p.push(sum1)
        elif x=='*':
            num1=p.pop()
            num2=p.pop()
            sum1=num2*num1
            p.push(sum1)
        elif x=='-':
            num1=p.pop()
            num2=p.pop()
            sum1=num2-num1
            p.push(sum1)
    print(p.items)



    

s=stack()
st1='6523+8*-3+*'
st2='a+b*c-(d/e+f)*g'
Postfix(st1)