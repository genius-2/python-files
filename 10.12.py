from random import randint
n = 3
m = 5
l=[[randint(1, 9) for i in range(n)] for i in range(m)]
for i in l:
    print()
    for j in i:
        print (j, end=" ")
c = 0
ind = 0
for i in range(n):
    for j in range(i):
        cn = l[i].count(l[i][j])
        if cn > c:
            c = cn
            ind = i
print()
print (c)
print (ind+1)
print("type 'end' to exit ")
e=str(input())   
    
