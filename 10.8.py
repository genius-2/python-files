s = input()
l = s.split(' ')
m = 0
c = 0
for i in range(len(l)):
    if len(l[i]) > m:
        m = len(l[i])
        c = i + 1
print (c)
print("type 'end' to exit ")
e=str(input())   

    