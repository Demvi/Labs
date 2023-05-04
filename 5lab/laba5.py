from random import randint

def z1():
    x = int(input('Введите число: '))
    xyz = [22, 1, 12, 123, 4444]
    if x in xyz:
        print('Вы угадали число!')
    else:
       print('вы не угадали')

#z1()

def z2():
    xxyz = [22, 12, 12, 123, 4444]
    for i in xxyz:
        if xxyz.count(i)>1:
            print(i)
#z2()

def z3():
    dni = ("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
    x = int(input("сколько выходых вы хотите в неделю? "))
    print(f"Ваши Рабочие дни: {dni[:-x]}")
    print(f"Ваши выходные дни: {dni[-x:]:}")
z3()