import os

from PIL import Image, ImageDraw, ImageFont
import qrcode
import shutil

from config.settings import BASE_DIR

def genImage(nombre,id,host,num):
    logo = qrcode.make('http://' + host + '/rifa/' + num + "/")
    logo = logo.resize((380, 380))
    logo = logo.crop((21, 23, 360, 360))

    img = Image.open(BASE_DIR + '/static/' + "flyer.png")
    # Escribe el Nombre
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(BASE_DIR + '/static/' + "arial.ttf", 100)
    font2 = ImageFont.truetype(BASE_DIR + '/static/' + "arial.ttf", 130)
    texto = str(nombre)
    texto2 = "Rifa N{}".format(num)

    # Centrar texto vertical y horizontalmente.
    lines = texto.splitlines()
    w = font.getsize(max(lines, key=lambda s: len(s)))[0]
    h = font.getsize(texto)[1] * len(lines)
    x, y = img.size
    x /= 2
    x -= w / 2
    y /= 2
    y -= h / 2

    lines = texto2.splitlines()
    w2 = font2.getsize(max(lines, key=lambda s: len(s)))[0]
    h2 = font2.getsize(texto2)[1] * len(lines)
    x2, y2 = img.size
    x2 /= 2
    x2 -= w2 / 2
    y2 /= 2
    y2 -= h2 / 2


    draw.multiline_text((x, 1370), texto, font=font, fill="white", align="center")
    draw.multiline_text((x2, 800), texto2, font=font2, fill="white", align="center")

    # Pega el Qr
    img.convert('RGBA')
    img.paste(logo, (370, 1000), logo)

    # guarda
    f = open(BASE_DIR + '/static/rifas/' + num + '.png', 'wb')

    img.save(f)
    f.close()

    return "{}.png".format(num)



