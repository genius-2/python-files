def Avr(a,b,c):
    Avr=(a + b + c)/3
    return Avr
a,b,c= map(int, input().split())
print("average")
print(Avr(a,b,c))
print("type 'end' to exit ")
e=str(input())