from random import randint

def one():
    x = int(input('Введите число: '))
    xyz = [22, 1, 12, 123, 4444]
    if x in xyz:
        print('Вы угадали число!')
    else:
       print('вы не угадали')

#one()

def two():
    xxyz = [22, 12, 12, 123, 4444]
    for i in xxyz:
        if xxyz.count(i)>1:
            print(i)
#two()

def three():
    dni = ("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
    x = int(input("сколько выходых вы хотите в неделю? "))
    print(f"Ваши Рабочие дни: {dni[:-x]}")
    print(f"Ваши выходные дни: {dni[-x:]:}")

three()

def four():
    k = 0
    list = ["Абийбиллаев", " Капров", "Иванов", " студент1", "студент2", " студент3", " студент4", " студент5", " студент6", " студент7" ]
    list1 = ["Черепов", " Иванов", " Исхаков", " студент8", "студент9", " студент10", " студент11", " студент12", " студент13", " студент14"]
    list2 = (list[0], list[1], list[0], list[5])
    print(list)
    print(list1)
    print(list2)
    print(len(list2))
    list2 = tuple(sorted(list2))
    print(list2)
    for i in range(len(list2)):
        if list2[i] == "Иванов":
            k += 1

    else:
        print('не встречается')


    print('встречается', k, 'раз')

four()
