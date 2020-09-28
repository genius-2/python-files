def a(n):
    d= (n-((n//3600)*3600))//60
    return d
n=int(input())
print(a(n))
print("type 'end' to exit ")
e=str(input())