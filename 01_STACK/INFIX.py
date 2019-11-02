from Class_Stack import stack

def hasHihgerPrec(top, found):
    if (top in '*/' and found in '-+') or (top in '+' and found in '-'):
        return True
    else:
        return False

def infixToPostfix(exp):
    s = list(exp)
    result = ''
    st = stack()
    for i in range(0, len(s)):
        print(st)
        if s[i] not in '+-*/':
            result += s[i]
        else:
            while (not st.isEmpty()) and hasHihgerPrec(st.peek(), s[i]):
                result += st.pop()
            st.push(s[i])
    
    while not st.isEmpty():
        result += st.pop()
    return result

def infixToPostfixWithPar(exp):
    s = list(exp)
    result = ''
    st = stack()
    for i in range(0, len(s)):
        if (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z'):
            result += s[i]
        elif s[i] == '(':
            st.push(s[i])
        elif s[i] in '+-*/':
            while (not st.isEmpty()) and hasHihgerPrec(st.peek(), s[i]) and (st.peek() != '('): 
                result += st.pop()
            st.push(s[i])
        elif s[i] == ')':
            while (not st.isEmpty()) and (st.peek() != '('):
                result += st.pop()
            st.pop()
    while (not st.isEmpty()):
        result += st.pop()
    return result


s1 = 'A+B*C-D*E'
s2 = 'A*((B-C)+D)'
s3=  '(a+b)*c/d'
s4='a+b*c-(d/e+f)*g'
res1 = infixToPostfix(s3)
res2 = infixToPostfixWithPar(s3)

print(res2)