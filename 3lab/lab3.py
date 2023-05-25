from random import randint


def one():
    slova = []
    while (one_word := str(input("Введите слова через Enter: \n(Введите stop для окончания)"))) !="stop":
        slova.append(one_word)

    print(" ".join(slova))

one()


def two():
 word = input("введите слово:")

 for i in range(len(word)):
    if word[i]=="Ф" or word[i]=="ф":
        print("Это редкое слово")
        break
    else:
        print("Это не редкое слово")
        break
two()

def three():
    uni=0


    print("Для завершения игры введите слово stop")
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f"{a} + {b} = ")

        res = input()

        if res == "stop":
            break
        res = int(res)
        if a + b == res:
            print("Правильно!")
        else:
            print("Ответ неправильный :(")
            uni = uni + 1
        if uni == 3:
           print('игра окончена')
           break

three()



