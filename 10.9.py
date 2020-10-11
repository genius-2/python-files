s = input()
l = []
m = 0
for i in range(len(s)):
    if s[i] in '1234567890':
        print(s[i])
        l.append(int(s[i]))
print (l)
for i in range(len(l)):
    if l[i] > m:
        m = l[i]
print (m)
print (sum(l))
print(len(l))
