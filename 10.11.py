from random import randint
n = 3
l=[[randint(1, 9) for i in range(n)] for i in range(n)]
for i in l:
    print()
    for j in i:
        print (j, end=" ")
print("type 'end' to exit ")
e=str(input())   
