from random import randint
n = 3
m = 5
l=[[randint(1, 9) for i in range(n)] for i in range(m)]
for i in l:
    print()
    for j in i:
        print (j, end=" ")
print("type 'end' to exit ")
e=str(input())   
    