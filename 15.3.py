class strvar:
    name = ""
    def set ( self , newName ):
        self.name = newName
    def get ( self ):
        return self.name
    def __init__(self, Name):
        self.name = Name
str = strvar (input())
print ( str.get ())
str.set (input("ведите имя"))
print ( "имя изменено на ", str.get ())