a = int(input())
s = 0
while a != 0:
    q = a % 10
    if q % 2 == 1:
        s = s + q*q
    a = a // 10
print (s)
print("type 'end' to exit ")
e=str(input())   
