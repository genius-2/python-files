l = [3, 6, 7, 4, -5, 4, 3, -1]
if sum(l) > 2:
    print (len(l))  
a = max(l)
b = min(l)
if abs(a-b) >= 10:
    l.sort()    
    print (l)
else: 
    print("разность меньше 10")
print("type 'end' to exit ")
e=str(input())