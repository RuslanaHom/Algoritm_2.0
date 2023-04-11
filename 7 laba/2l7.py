from PIL import Image, ImageFilter
Images = ['k1.jpg', 'k2.jpeg', 'k3.jpg', 'k4.jpg', 'k5.jpg']
for img in Images:
    fil = Image.open(img)
    fil1 = fil.filter(ImageFilter.FIND_EDGES)
    fil1.save('filters/' + str(img))

