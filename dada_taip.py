def changer(a,b):
    a = 2
    b[0] = 'Good'
x = 10 
L = [1,2 ]
changer(x, L)
print(x)
print(L)
L = [1,2]
changer(x, L[:])
print(L)

x = 3 
y = 4 
z = complex(x,y)
print(z)
w = complex(y,x)
print(z + w)
#str
s = 'sasdasdasdasdasddasdasdasd'
s = print(s[0])
#s[0] ='AAA'- errrorrr
#tuple 
t = (1,2,3)
print(t)
print(t[0])
#t[0]=3 errrorr
#list
l = [1,3,4]
l[0]=3
print(l)
#dict 
d = {'aa':4,4:'aa','str':'Hesda'}#ключ значение 
print(d['aa'])