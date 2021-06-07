'''
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
'''

a = 'attribute' #возможно записать в байтовом типе
ba = b'attribute'
print(type(ba))

k = 'класс'     # невозможно записать в байтовом типе, bytes can only contain ASCII literal characters
bk = 'класс'
print(type(bk))

f = 'функция'   # невозможно записать в байтовом типе, bytes can only contain ASCII literal characters
fk = b'функция'
print(type(fk))

t = 'type' #возможно записать в байтовом типе
bt = b'type'
print(type(bt))