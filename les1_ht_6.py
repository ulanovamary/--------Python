'''
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
 «декоратор».
 Проверить кодировку файла по умолчанию.
 Принудительно открыть файл в формате Unicode и
 вывести его содержимое
'''
import chardet

text = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w' ) as f:
    for el in text:
        f.write(el + ' ')

neededFile = open("test_file.txt", 'rb')
rawdata = neededFile.read()
result = chardet.detect(rawdata)
charenc = result['encoding']
print(result)
neededFile.close()

with open('test_file.txt', 'r') as f:
    line = f.readline()
    li = line.encode(encoding='utf-8').decode(encoding='utf-8')
    print(li)