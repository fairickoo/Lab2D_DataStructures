from Class_Stack import stack

def postfix(infix):
    s = stack()
    a = '' 
    count = 0 
    p=0
    for i in infix: 
        if i == '-': 
            count += 1
            while not s.isEmpty(): 
                if s.peek() == '-' or s.peek() == '(': 
                    break 
                else:
                    a += s.pop() 
            s.push('-') 
        elif i == '+': 
            count += 1
            while not s.isEmpty(): 
                if s.peek() == '+' or s.peek() == '-' or s.peek() == '(': 
                    break 
                else: 
                    a += s.pop() 
            s.push('+') 
        elif i == '/' : 
            count += 1 
            while not s.isEmpty(): 
                if s.peek() == '/' or s.peek() == '+' or s.peek() == '-' or s.peek() == '(':
                    break 
                else: 
                    a += s.pop() 
            s.push('/')
        elif i == '*':
            count += 1
            if not s.isEmpty():
                while not s.isEmpty():
                    if s.peek() == '*' or s.peek() == '/' or s.peek() == '+' or s.peek() == '-' or s.peek() == '(': 
                        break
                    a += s.pop()
            s.push('*')
        elif i == '(': 
            s.push(i) 
        elif i == ')': 
            while s.peek() != '(' and not s.isEmpty(): 
                a += s.pop() 
            s.pop() 
        else: 
            if i != ' ': 
                a += i 

    while(not s.isEmpty()):
        a += s.pop() 
    for x in a:
        if x>='a' and x<='z':
            p+=1

    print('Result postfix expression : ',a) 
    print('Number of operation       : ',count)
    print('Number of operand         : ',p)



infix = str(input('Enter infix expression    :  '))
postfix(infix)