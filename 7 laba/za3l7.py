from PIL import Image, ImageFilter
images = [Image.open("k1.jpg"), Image.open("k2.jpeg."),
          Image.open("k3.jpg"), Image.open("k4.jpg"), Image.open("k5.jpg")]
for i, img in enumerate(images):
    img.show()
    img = img.filter(ImageFilter.FIND_EDGES)
    mini = f'new_{i+1}.jpg' #форматная строка
    print(mini)
    img.save(f'C:/Pycharm/7 laba/{mini}')