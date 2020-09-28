def s(a,b):
    s=a*b
    return s
def p(a,b):
    p=2*(a+b)
    return p
a,b=map(int, input().split())
print("area is")
print(s(a,b))
print("perimeter is")
print(p(a,b))
print("type 'end' to exit ")
e=str(input())
