def ToF(cel):
    far = 9/5 * cel + 32
    return far
cel=int(input())
print("in farenheit: ")
print(ToF(cel))
print("type 'end' to exit ")
e=str(input())