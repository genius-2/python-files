def If(s, n):
    if n > len(s):
        print(s.upper())
    else:
        print(s)
    return 0;
s = str(input())
n = int(input())
If(s, n)
print("type 'end' to exit ")
e=str(input())