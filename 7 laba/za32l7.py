from PIL import Image, ImageFilter
image1 = Image.open("k3.jpg")
image1.show()
mini_image = image1.filter(ImageFilter.FIND_EDGES)
mini_image.save("D:/k32.jpg")
mini_image.show()