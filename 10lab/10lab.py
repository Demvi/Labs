import json

def one_two():
    with open ("ddd.json", "r") as k:
        h = json.load(k)
        for i in h['products']:
            print("\nНазвание: " + i['name'])
            print("Цена: " + str(i['price']))
            print("вес: " + str(i['weight']))
            if i['available']:
                print("В наличии")
            else:
                print("Нет в наличии!")

        x = input("Хотите добавить товар? да/нет : ")
        if x == "да":
            with open("ddd.json", "w") as l:
                name = input("Введите название товара: ")
                price = input("Введите цену товара: ")
                weight = input("Введите вес товара: ")
                p = input("Товар есть в наличии? да/нет : ")
                if p =="да":
                    available = True
                else:
                    available = False
                h['products']
                l.write(json.dumps(h))

one_two()