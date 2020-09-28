def solve(a1, b1, c1, a2, b2, c2):
    D = (a1*b2) - (a2*b1)
    x = ((c1*b2) - (c2*b1))/D
    y = ((a1*c2) - (a2*c1))/D
    return x,y
a1, b1, c1, a2, b2, c2=map(int, input().split())
print(solve(a1, b1, c1, a2, b2, c2))
print("type 'end' to exit ")
e=str(input())