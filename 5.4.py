def solve(x):
    if -2.4 <= x <= 5.7:
        return x*x
    else:
        return 4
x=float(input())
print(solve(x))
print("type 'end' to exit ")
e=str(input())