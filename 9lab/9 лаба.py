import pathlib

def one():
    spisok = ["1.png","2.jpg","3.png","4.jpg","5.png"]

    for i in spisok:
        image = Image.open(i)

        image = image.filter(ImageFilter.CONTOUR)
        #image.show()




