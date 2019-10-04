from Class_Queue import queue



def decode(word,q):
    s=queue()
    out=''
    for x in q:
        s.enqueue (x)
    for x in word:
        if (ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=122):
            t=s.dequeue()
            s.enqueue(t)
            if (ord(x)>=97 and ord(x)<=122)and ((ord(x)+t)>122):
                out+=chr(ord(x)+(t-26))
            elif  (ord(x)>=65 and ord(x)<=90)and ((ord(x)+t)>90):
                out+=chr(ord(x)+(t-26))
            else:
                out+=chr(ord(x)+t)
        elif ord(x)==32:
            out+=' '
    return out

def encode(word,q):
    s=queue()
    out=''
    for x in q:
        s.enqueue (x)
    for x in word:
        if (ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=122):
            t=s.dequeue()
            s.enqueue(t)
            if (ord(x)>=97 and ord(x)<=122)and ((ord(x)-t)<97):
                out+=chr(ord(x)-(t-26))
            elif  (ord(x)>=65 and ord(x)<=90)and ((ord(x)-t)<65):
                out+=chr(ord(x)-(t-26))
            else:
                out+=chr(ord(x)-t)
        elif ord(x)==32:
            out+=' '
    return out




word='I love Python'
st1=[2,5,6,1,8,3]
st2=[2,5,6,1,8,3]
print('SEN   : ',word)
print('SHIP  :  2 5618 325618')
print('decode: ',decode(word,st1))
print('encode: ',encode(decode(word,st1),st2))