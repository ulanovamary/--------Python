'''
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
'''
words = ['разработка', 'администрирование', 'protocol', 'standard']
def decoder(word:str):
    print(type(word), word)

    bword = word.encode(encoding='utf-8')
    print(type(bword), bword)

    uword = bword.decode(encoding='utf-8')
    print(type(uword), uword)


if __name__ == "__main__":
    for i in words:
        decoder(i)
