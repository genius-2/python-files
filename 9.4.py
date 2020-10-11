l = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
if 'привет' in l:
    l.remove('привет')
    print(l)
else:
    l.append('привет')
if l.count(4)>1:
    l.clear()
    print(l)
print("type 'end' to exit ")
e=str(input())  