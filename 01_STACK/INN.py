from Class_Stack import stack
def infixToPostfix():
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    postfix = ''
    for c in infix:
        if c.isalpha():
            postfix += c
        elif c == '(':
            s.push(c)
        elif c == ')':
            while s.pop() != '(':
                postfix += s.pop()
                s.pop()
        else:
            while (not s.isEmpty() and prec[s.peek()]>=prec[c]):
                postfix += s.pop()
            s.push(c)
            
    while not s.isEmpty():
        postfix += s.pop()
    return postfix
def operation():
    numOfOperation = 0
    for i in infix:
        if i in '+-*/':
            numOfOperation +=1
    return str(numOfOperation)
def operand():
    numOfOperand = 0
    for i in infix:
        if i in 'abcdefg':
            numOfOperand += 1
    return str(numOfOperand)
s = stack()   
infix = input('Enter infix expression : ')
print('Result postfix expression : ' + infixToPostfix())
print('Number of operation : ' + operation())
print('Number of operand : ' + operand())