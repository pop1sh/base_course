a = int(input('Первый член'))
b = int(input('Знаменатель'))
c = int(input('Кол-во членов'))
print(a)
for i in range (1,c):
    a*=b
    print(a)