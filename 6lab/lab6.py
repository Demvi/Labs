from random import randint

def one():
    countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                 "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                 "Северная Македония": "Скопье", "Сербия": "Белград"}

    for i in sorted(countries_dict):
        print(i + ' : ' + countries_dict[i])

    x = input("Введите страну: ")
    print('Столица: ' + countries_dict[x])



def two():
    y = input('Введите ваше слово: ').lower()
    alp = {
        "авеинорст": 1,
        "дклмпу": 2,
        "бгёья": 3,
        "йы": 4,
        "жзхцч": 5,
        "шэю": 8,
        "фщъ": 10
    }
    s = 0
    for i in y:
        for j in alp:
            for k in j:
                if k == i:
                    s+=alp[j]

    print(s)

#two()

def three():
    stud = {"Петров":[],
            "Иванов":[],
            "Лебедев":[],
            "Цзиньпин":[],
            "Абийбилаев":[]
            }
    lang = ["Английский", "Китайский", "Кыргызский", "Испанский", "Немецкий"]
    for i in stud:
        p = randint(0,4)
        l = randint(0,4)
        for j in range(p):
            l = randint(0, 4)
            if lang[l] not in stud[i]:
                stud[i].append(lang[l])
    print(stud)
    q=0
    for i in lang:
        for j in stud:
            if i in stud[j]:
                q += 1
        print(f'Студентвов знающих {i}: {q}')
    q=0

    print("Студенты знающие Китайский: ")
    for i in stud:
        if "Китайский" in stud[i]:
            q+=1
            print(i)


#one()
#two()
three()