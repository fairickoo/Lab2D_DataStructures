from Class_Stack import stack


def InfixToPostfix(word):
    s=stack()
    p=stack()
    out=''
    for x in word:
        s.push(x)
    print('Enter infix expression   :',s)

    for x in range(s.__len__()):
        if s.items[x]>='a' and s.items[x]<='z':
            out+=s.items[x]
        else:
            print('item no :',s.items[x])
            if s.items[x]=='+' or s.items[x]=='-' or s.items[x]=='*' or s.items[x]=='/' or s.items[x]=='(' or s.items[x]==')' :
                if p.isEmpty():
                    p.push(s.items[x])
                    print('head',p)

                else:
                        if(str(p.items[0])=='+' or str(p.items[0])=='-') and (s.items[x]=='*' or s.items[x]=='/' ):
                            print('-------------------[+-  x= * ]')
                            p.push(s.items[x])
                            print('stack',p)
                        elif (str(p.items[0])=='+' or str(p.items[0])=='-')and (str(p.items[1])=='*' or str(p.items[1])=='/'):
                            if (s.items[x]=='+' or s.items[x]=='-' ):
                                print('-------------------[+-,*/  x= +- ]')
                                x1pop=p.pop()
                                x2pop=p.pop()
                                out+=x1pop+x2pop
                                p.push(s.items[x])
                                print('stack',p)
                        elif  (str(p.items[0])=='()' or str(p.items[0])=='-'):
                            pass
                            
    out+=str(p)
    print('Result postfix expression    :',out)
        



st1='a+b*c-d'
st2=' a+b*c-(d/e+f)*g'
st3='(a+b)*c/d'
st4='+*-'
InfixToPostfix(st2)
    