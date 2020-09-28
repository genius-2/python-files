def comp(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return "="
a,b=map(int, input().split())
print(comp(a,b))
print("type 'end' to exit ")
e=str(input())