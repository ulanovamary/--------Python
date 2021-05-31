'''
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
'''
if __name__ == '__main__':

    bclass = b'class'
    bfunction = b'function'
    bmethod  = b'method'

    print(type(bclass), bclass, len(bclass), type(bfunction), bfunction, len(bfunction), type(bmethod), bmethod, len(bmethod))



