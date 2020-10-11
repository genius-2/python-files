l = [-8, 8, 6.0, 5, 'строка', -3.1]
s = 0
for i in l:
if type(i) == int:
s = s + i
elif type(i) == float:
s = s + i
print (s)
print("type 'end' to exit ")
e=str(input())