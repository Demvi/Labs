from PIL import Image, ImageDraw, ImageFont


def one():
    im = Image.open('9mai.jpg')
    im_crop = im.crop((10, 10, 300, 400))
    im_crop.save('9may.jpg')
    im_crop.show()



def two():
    spisok = {"День победы": "9mai.jpg", "Праздник всех женщин":"8mart.jpg", "Новый год": "NG.png", "День рождение": "brtd.jpg"}

    x = input("Какой сейчас праздник? ")

    if x in spisok:
        image = Image.open(spisok[x])
        image.show()
    else:
        print("Такой открытки нет")


def three():

    name = input("Введите имя получателя: ")
    filename = "brtd.jpg"

    with Image.open(filename) as img:
        img.load()

    font = ImageFont.truetype("arial.ttf", 30)
    draw_text = ImageDraw.Draw(img)

    draw_text.text((img.width // 2 - 100, 15),name + ", поздравляю!", font=font, fill=('green'))

    img.show()
    img.save(name + "brtd2.png")

one()
two()
three()


