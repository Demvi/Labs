from PIL import Image, ImageFilter

def one():

    image = Image.open("1.png")
    image.show()

    print( image.format, image.size, image.mode)
#one()

def two():
    image = Image.open("2.jpg")

    image2 = image
    newW = image.size[0]
    newH = image.size[1]
    image2 = image2.resize([newW,newH])
    image2.save("2min.jpg")

    image3 = image.transpose(Image.FLIP_LEFT_RIGHT)
    image3.save("2zerk.jpg")

    image4 = image.transpose(Image.FLIP_TOP_BOTTOM)
    image4.save("2zerk2.jpg")
#two()

def three():
    spisok = ["1.png","2.jpg","3.png","4.jpg","5.png"]

    for i in spisok:
        image = Image.open(i)

        image = image.filter(ImageFilter.CONTOUR)
        image.show()
#three()

def four():

    image = Image.open("2.jpg")
    watMark = Image.open("6.png")


    watMark = watMark.resize([100,100])
    image.paste(watMark, [100,100], mask=watMark)
    image.show()



#four()