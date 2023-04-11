from PIL import Image
image = Image.open("D:\homyaki\h1.jpg.") #Открывает изображение
image.show()
size = image.size #размер картинки
format = image.format #формат картинки
mode = image.mode #мод(RGBA)
arr = [] #пустой массив
arr.append(size)  #доб. размер в массив
arr.append(format) #доб. формат в массив
arr.append(mode)  #доб. мод в массив
print(arr) #вывод массива