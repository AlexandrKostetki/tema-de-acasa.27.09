from lzma import MF_BT4


a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
def divizor(m,n,f):
    l1=[]
    for i in range (1, int(max(m,n,f)/2)+1):
        if n% i ==0 and m %i ==0:
            l1.append(i)
        return l1

print("a) un divizor comun:", divizor(a,b,c))

def multiplu(m,n,f):
    mm=[]
    mn=[]
    mf=[]
    tot=[]

    for i in range (1, max(m,n,f)):
        mm.append(m*i)
        mn.append(n*i)
        mf.append(f*i)
    
    for i in mm:
        if i in mn and i in mf:
            tot.append(i)

    return tot[0:1]

print("b) un multiplu comun:",multiplu(a,b,c))

def minim(m,n,f):
    if m>f and n>f:
        return f
    if m>n and f>n:
        return n
    if f>m and n>m:
        return m
    else:
        return print('n si f sunt la fel')

print("c)Minim:",minim(a,b,c))

def maxim(m,n,f):
    if m<f and n<f:
        return f
    if m<n and f<n:
        return n
    if f<m and n<m:
        return m
    else:
        return print('x si y sunt la fel')

print("d)Maxim:",maxim(a,b,c))

def treimultiplu(m,n,f):
    mm=[]
    mn=[]
    mf=[]
    tot=[]

    for i in range (1, max(m,n,f)):
        mm.append(m*i)
        mn.append(n*i)
        mf.append(f*i)
    
    for i in mm:
        if i in mn and i in mf:
            tot.append(i)

    return tot[0:3]

print("e)3 multipli comuni:",treimultiplu(a,b,c))





def ecuatia(m,n,f):

    delta=n**2-4*m*f
    x1=(-n-math.sqrt(delta))/m
    x2=(-n+math.sqrt(delta))/m
    xx=-n/2*m
    if delta > 0 :
        return print('h)x1=',x1,'x2=' ,x2)
    if delta ==0 :
        return print('h)x=', xx)
    if delta < 0 :
        return print('h)Solutie vida')

print(ecuatia(a, b, c))