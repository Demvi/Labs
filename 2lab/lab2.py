def one():
    password = input('Введите пороль: ')

    is_numeric = False
    is_upper = False
    is_lower = False
    is_spec = False

    for tap in password:
        if tap.isnumeric():
            is_numeric = True
        elif tap.islower():
            is_lower = True
        elif tap.isupper():
            is_upper = True
        elif tap in "#%&@$^*":
            is_spec = True

    if len(password) > 6 and is_numeric and is_upper and is_lower and is_spec:
        print('Пароль : Надежный ')
    else:
        print('Пароль не очень надежный , попробуйте еще раз')


one()

def two():
    des = int(input('Введите номер вашего места вагоне: '))
    
    if des >= 36:
        print('Ваше место - боковое.')
    elif des % 2:
        print('Ваше места в купе внизу')
    else:
        print('Ваше место в купе наверху ')


two()


def three():
    year = int(input("Введите день: "))

    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('Высокосный')
    else:
        print('Не высокосный')


three()


def four():
    zvet1 = input('Введи первый цвет')
    zvet2 = input('Введи второй цвет')

    if (zvet1 == 'красный' or zvet2 == 'красный') and (zvet1 == 'синий' or zvet2 == 'синий'):
        print('фиолетовый')
    elif (zvet1 == 'красный' or zvet2 == 'красный') and (zvet1 == 'желтый' or zvet2 == 'желтый'):
        print('оранжевый')
    elif (zvet1 == 'синий' or zvet2 == 'синий') and (zvet1 == 'желтый' or zvet2 == 'желтый'):
        print('зеленый')
    elif zvet1 == zvet2 and (zvet1 == 'синий' or zvet1 == 'красный' or zvet1 == 'желтый'):
        print(zvet1)
    else:
        print('Ошибка в выборе цвета')


four()