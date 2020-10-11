from random import randint
a=randint(1,10)
q=int(input("Угадайте целое число от 1 до 10:"))
while q!=a:
    if q<a:
            print("Ваше число меньше, чем задумал компьютер")
    elif q>a:
            print("Ваше число больше, чем задумал компьютер")
    else:
            print("Вы угадали")
    q = int(input("повторите"))
print("type 'end' to exit ")
e=str(input())   
