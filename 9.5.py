from random import choice
l = ['самовар', 'весна', 'лето']
s=choice(l)
b=choice(s)
a = s.index(b)
print(s[0:a] +'?' +s[a+1:len(s)])
print ("введите букву")
q = str(input())
if b==q:
    print ("правильно!")
else:
    print ("не правильно!")
print("type 'end' to exit ")
e=str(input())      