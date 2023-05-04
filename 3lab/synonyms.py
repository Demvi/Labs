import random


z = True
i = 0
slovo = input('введите ваше слово: ')


with open('synonyms.txt','r') as f:
    lines = len(f.readlines())

with open('synonyms.txt','r') as f:
    u = f.read()

with open('synonyms.txt','r') as f:
    while z == True:

        x = f.readline()

        if slovo.upper() in x.upper():
            z = False

            con = x.split(" ")
            p = random.randint(3,len(con))-1
            print(con[p])

            y = input('Понравился ли вам подбор синонома? да/нет: ')

            if y == 'нет':
                a = str(input('Пожалуйста, введите слово синоним: '))
                with open('synonyms.txt','wt') as f:
                    u = u.replace(x, x[:-1]+'; '+a+'\n')

            break

        if i == lines:
            print("вашего слова не найдено")
            break
        i+=1
#print(u)

with open('synonyms.txt', 'w') as f:
    f.write(u)
