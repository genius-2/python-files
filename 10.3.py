l = []
n = int(input())
for i in range(n):
    a = int(input())
    l.append(a)
if n % 2 != 0:
    print ("поменять нельзя")
else: 
    print(l[n // 2 :] + l[0: n // 2])
print("type 'end' to exit ")
e=str(input())   