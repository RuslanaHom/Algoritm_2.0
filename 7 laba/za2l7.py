from PIL import Image
image = Image.open("D:\homyaki\h2.jpg.")
image.show()
new_image = image.resize((640, 425))
new_image.show()
new_image.save('D:/hom.jpg') #уменьшение масштаба картинки в три раза и сохранение
image_2 = image.transpose(Image.FLIP_TOP_BOTTOM)
image_2.show()
image_2.save('D:/hom2.jpg') #Отзеркаливание по горизонтали
image_3 = image.transpose(Image.FLIP_LEFT_RIGHT) #отзеркаливание по вертикали
image_3.show()
image_3.save('D:/hom3.jpg')



