from PIL import Image
image = Image.open("C:hom.jpg.")
logo = Image.open("C:emb.png.")
image.paste(logo, (0, 0), mask=logo)
image.show()
