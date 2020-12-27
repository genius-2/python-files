import random
zoo = []
class lion():
    def __init__(self,name):
        print('Родился лев  ')
        self.name= name
        self.weight= random.randint(50,150)
        self.growth = random.randint(80,100)
        zoo.append(self.name)
    def caress(self):
        print("лев откусил вам руку")
    def visit(self):
        print('лев в порядке его зовут',self.name)
class tiger():
    def __init__(self,name):
        print('Родился тигр')
        self.name= name
        self.weight= random.randint(50,150)
        self.growth = random.randint(80,100)
        zoo.append(self.name)
    def caress(self):
        print("вы гладите тигра")
    def visit(self):
        print('тигр в порядке его зовут',self.name)
class pinguin():
    def __init__(self,name):
        print('родился пингвин')
        self.name= name
        self.weight= random.randint(50,150)
        self.growth = random.randint(80,100)
        zoo.append(self.name)
    def caress(self):
        print("вы гладите пингвина")
    def visit(self):
        print('пингвин в порядке его зовут',self.name)

def main():
    a = 1
    while a != 0:
        x = int(input("вы в зоопарке что хотите: 1 - добавить животное ,2 - удалить животное,3 - список, 4 - выход "))
        if x == 2:
            x = str(input("Введите имя"))
            for i in range(len(zoo)):
                if zoo[i] == x:
                    zoo.remove(zoo[i])
        elif x == 3:
            print(zoo)
        elif x == 1:
            new = None
            while new != 0:
                k = int(input("Кого хотите добавить? 1 - лев 2 - тигр 3 - пингвин,4 - вернутся назад"))
                if k == 1:
                    aname = input("Дайте имя животному ")
                    ani = lion(aname)
                    todo = None
                    while todo != 0:
                        l = int(input("что с ним делать 1 - навестить , 2-погладить,3 - инфо, 4 - ничего "))
                        if l == 1:
                            ani.visit()
                        elif l == 2:
                            ani.caress()
                        elif l == 3:
                            print("Имя:", ani.name)
                            print("Рост:", ani.growth)
                            print("Вес:", ani.weight)
                        elif l == 4:
                            todo = 0
                elif k==2:
                    aname = input("Дайте имя животному ")
                    ani = tiger(aname)
                    todo = None
                    while todo != 0:
                        l = int(input("что с ним делать 1 - навестить , 2-погладить,3 - инфо, 4 - ничего "))
                        if l == 1:
                            ani.visit()
                        elif l == 2:
                            ani.caress()
                        elif l == 3:
                            print("Рост:", ani.growth)
                            print("Вес:", ani.weight)
                        elif l == 4:
                            todo = 0
                elif k == 3:
                    aname = input("Дайте имя животному ")
                    ani = pinguin(aname)
                    todo = None
                    while todo != 0:
                        l = int(input("что с ним делать 1 - навестить , 2-погладить,3 - инфо, 4 - ничего "))
                        if l == 1:
                            ani.visit()
                        elif l == 2:
                            ani.caress()
                        elif l == 3:
                            print("Рост:", ani.growth)
                            print("Вес:", ani.weight)
                        elif l == 4:
                            todo = 0
                else:
                    new = 0

        else:
            a = 0
main()