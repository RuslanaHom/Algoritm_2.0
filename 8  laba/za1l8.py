from PIL import Image
image = Image.open('C:/Pycharm/otk.jpg')
image.show()
im_crop = image.crop((100, 100, 400, 300)) #лево, верх, право, лево
im_crop.save('C:/Pycharm/otk_crop.jpg',)
im_crop.show()
