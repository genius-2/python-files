class Animal:
    nickname=""
    def walk(this):
        print(this.nickname," делает Топ топ топ")
    def rename(this, newnickname):
        this.nickname = newnickname
        print("его теперь зовут", this.nickname)
    def renickname(this):
        return this.nickname
    def toSleep(this):
        print(this.nickname + " zzz")
    def __init__(this,newnickname):
        this.nickname=newnickname
        print("Родился лев " + this.nickname)

lion=Animal("Рыжь")
lion.walk()
print(lion.renickname())
lion.rename("Алекс")
print(lion.renickname())
lion.toSleep()