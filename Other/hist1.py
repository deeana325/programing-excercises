l=[1,2,3]
l
1 in l
10 in l
x=10
x+=5
x
x-=5
x
x/=2
x
x*=5
x
s='abc'
s+=' '
s
s*10
s*=10
s
s[:4]
l
l+=5
l+=[5]
l
l+l
l
l[0]
l[4]
l[4]
l[3]
len(l)
l[len(l)]
l[len(l)-1]
l[-1]
l[-2]
l[0:1]
L[0]
l[0]
l[0:2]
l[0:-1]
l[0:-2]
l[0:4]
l[0:len(l)]
l[:2]
l[2:]
l[:]
s='abcdef'
s[:4]
s[2:3]
s[1:3]
s[-2:]
tuple(l)
type(l)
type(s)
type(tuple(l))
type(1)
str(l)
str(1)
bool(1)
bool(0)
bool('str')
bool('')
bool(123)
type(1.1)
2.3199434e7
645645646489779878978964564564*2
bool
False and False
False and True
True and True
True or False
True or not False
l=[1,2,3,4]
for x in l:
    print(x)

m=l[1]
for x in l:
    if m>x:
        m=x
print(m)

def minim(l):
    m=l[0]
    for x in l:
        if m>x:
            m=x
    return m
minim([4,6,2,1,0,-40,-2])

def maxim(l):
    m=l[0]
    for x in l:
        if m<x:
            m=x
    return m

maxim([4,6,2,1,0,-40,-2])
minim?
minim??
max([4,6,2,1,0,-40,-2])
max??
minim(['c','a','bb'])
max?
None
v==None
v=None
v
type(v)
type(print('abc'))
type(minim([1,2,50]))
int(2.1)
int(2.6)
round(2.6)
round(2.6492347, 1)
round(2.6492347, 2)
str(2.6492347)
str(2.6492347)[:4]
x=2.6492347
int(x*100)
int(x*100)/100
10**3
x=x==2
x
type(x=2)
x:=2
t=(1,2,3)
type(t)
t
a,b,c=t
a
b
c
a,b,c=
a,b,c=7,8,9
a
b
c
hist
def minmax(l):
    minim=l[0]
    maxim=l[0]
    for x in l:
        if maxim<x:
            maxim=x
        if minim>x:
            minim=x    
    return minim,maxim

minmax([4,6,2,1,0,-40,-2])
a,b=minmax([4,6,2,1,0,-40,-2])
a
b
minim,maxim=minmax([4,6,2,1,0,-40,-2])
minim
maxim
minim, maxim = minmax([4, 6, 2, 1, 0, -40, -2])

def minmax(l):
    minim = l[0]
    maxim = l[0]
    for x in l:
        if maxim < x:
            maxim = x
        if minim > x:
            minim = x    
    return minim, maxim
sum([4, 6, 2, 1, 0, -40, -2])
sum('ab','cd','efg')
sum(['ab','cd','efg'],'hi')
sum(['ab','cd','efg'])
sum(['ab','cd','efg'], '')
sum(['ab','cd','efg'], [])
sum?
sum(['ab','cd','efg'], '')
'',join(['ab','cd','efg'])
''.join(['ab','cd','efg'])
d={'prenume': 'Diana', 'nume': 'Cristescu'}
d
type(d)
len(d)
d['nume']
d['prenume']
d.keys
d.(keys)
d.keys()
d.values()
d.items
d.items()
for x in d:
    print(x)
for x in d:
    print(x,d[x])
d={'prenume': 'Diana', 'nume': 'Cristescu', 123:[1,2,3]}
d
for x in d:
    print(x,d[x])
d={'prenume': 'Diana', 'nume': 'Cristescu', 123:[1,2,{'super': 'duper'}]}
d
d[123}
d[123]
d[123][2]
d[123][2]['super']
''.join(['wo9rh','jkadg'])
'---'.join(['wo9rh','jkadg'])
'wo9rh---jkadg'.split('-')
import datetime
type(datetime)
type(datetime.datetime)
type(datetime.datetime.mnow)
type(datetime.datetime.now)
