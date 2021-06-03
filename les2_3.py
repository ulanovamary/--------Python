'''
Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
 второму — целое число, третьему — вложенный словарь,
 где значение каждого ключа — это целое число с юникод-символом,
 отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
'''
import yaml


data_to_yaml = {
    'first': [1,2],
    'second': 6,
    'third': {
        '€':'John',
        '€€': '22'
    },
}
print('before changes ' + str(data_to_yaml))

with open('file.yaml', 'w') as f_n:
    try:
        for key, value in data_to_yaml.items():
            if isinstance(value, dict):
                str(value).encode('utf-8').decode('utf-8')
            if type(value) is list:
                [str(x).encode('utf-8').decode('utf-8') for x in value]
        else:
            str(key).encode('utf-8').decode('utf-8'), str(value).encode('utf-8').decode('utf-8')
            yaml.dump(data_to_yaml, f_n, default_flow_style=False, allow_unicode = True)
    except UnicodeEncodeError as e:
        print('!!!')

with open('file.yaml') as f_n:
    print(f_n.read())