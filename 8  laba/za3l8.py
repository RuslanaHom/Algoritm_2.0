from PIL import Image, ImageFont, ImageDraw
image = Image.open('C:/Pycharm/photo.jpg')
image.show()

text = input('Введите имя для поздравления: ')
draw = ImageDraw.Draw(image)
font1 = ImageFont.truetype('times', 80)
font2 = ImageFont.truetype('impact', 95)
new = f'{text},'
draw.text((245, 470), new, (219, 85, 130), font=font1, stroke_width=4, stroke_fill=(219, 85, 130))
draw.text((245, 620), 'Поздравляю!', (0, 255, 255), font=font2, stroke_width=2, stroke_fill=(255, 0, 255))
image.save('C:/Pycharm/otk.png')
