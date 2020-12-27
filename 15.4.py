class dot:
    х = 0
    у = 0
    def establishX ( self , X ):
        self.х = X
    def establishY ( self , Y ):
        self.у = Y
    def receiveX ( self ):
        return self.x
    def receiveY ( self ):
        return self.у
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

x=int(input("Введите x:"))
y=int(input("Введите y:" ))
Dot = dot(x, y)
Dot.establishX(x)
Dot.establishY(y)
print(Dot.receiveX())
print(Dot.receiveY())