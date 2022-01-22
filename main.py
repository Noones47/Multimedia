from PIL import Image, ImageEnhance


def blackwhite():
    # Abrir a imagem
    image = Image.open("img1.jpg")
    img_data = image.getdata()

    # Percorrer a imagem
    lst = []
    for i in img_data:
        lst.append(i[0] * 0.2125 + i[1] * 0.7169 + i[2] * 0.0689)

    # Cria uma nova imagem
    new_image = Image.new("L", image.size)
    new_image.putdata(lst)

    # Guarda a imagem
    new_image.save("bw.jpg")



def negativo():

    image = Image.open("img3.jpg")

    # Percorrer a imagem
    for i in range(0, image.height - 1):
        for j in range(0, image.width - 1):
            # OBTER VALOR DO PIXEL (X,Y)
            pixelColorVals = image.getpixel((i, j))

        # INVERTER COR
            redPixel = 255 - pixelColorVals[0]
            greenPixel = 255 - pixelColorVals[1]
            bluePixel = 255 - pixelColorVals[2]

        # Modificar a imagem com os valores invertidos

            image.putpixel((i, j), (redPixel, greenPixel, bluePixel))
    # Guardar a imagem

    image.save("negative1.jpg")
    image.show()

def add():
    # Abrir as imagens
    image1 = Image.open("img1.jpg")
    image2 = Image.open("img2.jpg")


    # Percorre a imagem e guarda os pixeis
    for i in range(0, 512):
        for j in range(0, 512):
            pixelimg1 = image1.getpixel((i, j))
            pixelimg2 = image2.getpixel((i, j))

        # Soma os pixeis e guarda
            R = pixelimg1[0] + pixelimg2[0]
            if (R > 255):
                R = 255

            G = pixelimg1[1] + pixelimg2[1]
            if (G > 255):
                G = 255

            B = pixelimg1[1] + pixelimg2[1]
            if (B > 255):
                B = 255

        # Guarda a imagem
            image1.putpixel((i, j), (R, G, B))
    image1.save("adicao.jpg")


def sub():
    # Abrir as imagens
    image1 = Image.open("img1.jpg")
    image2 = Image.open("img2.jpg")


    # Percorre a imagem e guarda os pixeis
    for i in range(0, 512):
        for j in range(0, 512):
            pixelimg1 = image1.getpixel((i, j))
            pixelimg2 = image2.getpixel((i, j))

        # Soma os pixeis e guarda
            R = pixelimg1[0] - pixelimg2[0]
            if (R > 255):
                R = 255

            G = pixelimg1[1] - pixelimg2[1]
            if (G > 255):
                G = 255

            B = pixelimg1[1] - pixelimg2[1]
            if (B > 255):
                B = 255

        # Guarda a imagem
            image1.putpixel((i, j), (R, G, B))
    image1.save("subtracao.jpg")


def OR():
    # Abre as imagens
    img1 = Image.open("img1.jpg")
    img2 = Image.open("img2.jpg")


    # Percorre os pixeis e guarda
    for i in range(0, 512):
        for j in range(0, 512):
            pixelimg1 = img1.getpixel((i, j))
            pixelimg2 = img2.getpixel((i, j))

        # Filtra os pixeis pelo maior e seleciona o maior
            if (pixelimg1[0] > pixelimg2[0]):
                R = pixelimg1[0]
            else:
                R = pixelimg2[0]

            if (pixelimg1[1] > pixelimg2[1]):
                G = pixelimg1[1]
            else:
                G = pixelimg2[1]

            if (pixelimg1[2] > pixelimg2[2]):
                B = pixelimg1[2]
            else:
                B = pixelimg2[2]

        # Guarda a imagem
            img1.putpixel((i, j), (R, G, B))
    img1.save("or.jpg")



def blue():

        image = Image.open('img3.jpg')
        # show the image (optional)

        # load the image into memory
        image_data = image.load()
        # obtain sizes
        height, width = image.size
        # loop over and change blue value to 0
        for i in range(height):
            for j in range(width):
                r, g, b = image_data[i, j]
                image_data[i, j] = 0, 0, b
        # return image
        image.save('blue.jpg')
        image.show()









