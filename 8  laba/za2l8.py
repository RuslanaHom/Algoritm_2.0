from PIL import Image
holidays = {
    'День рождения': 'C:/hp.jpg',
    '8 марта': 'C:/8march.jpg',
    '9 мая': 'C:/9m.jpg',
    'Масленница': 'C:/mas.jpg'
}
p = input('Напишите праздник: ')
holidays2 = holidays.get(p)
if holidays2:
    image = Image.open(holidays2)
    image.show()
else:
    print('Открытка не найдена, перепроверьте правильность написания запроса')
