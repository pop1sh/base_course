a=int(input())
b=int(input())
if a%b==0:
    print('Делится нацело')
else:
    print('Не делится нацело','Остаток:', (a/b)-a//b)
print(a/b)
