'''
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт,
 автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
'''
import json
import datetime

def write_order_to_json(item, quantity, price, buyer, date:datetime.date):
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date,
    }

    with open('orders.json', 'w', ) as f_n:
        json.dump(dict_to_json, f_n, indent=4)

    with open('orders.json') as f_n:
        print(f_n.read())


if __name__ == "__main__":
    write_order_to_json('drumm', 5, 4.99, 'Johnson', (2005, 7, 14))
