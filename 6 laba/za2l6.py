dict_with_letter ={1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
word = input('Введите слово: ')
print(sum([kol for i in word for kol, v in dict_with_letter.items() if i in v]))

