import json


def load_data(path="operations.json"):
    '''функция чтения json файла'''
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_sort(data):
    '''функция сортировки по выполненым операциям и дате (последние 5)'''
    data = [item for item in data if item.get('state') == 'EXECUTED']
    data = sorted(data, key=lambda item: item['date'], reverse=True)
    return data[:5]


def formatted_data(item):
    '''оформляет дату, счет, карту, сумму, валюту в заданном порядке'''
    item_date = format_date(item.get("date"))

    if item.get("from"):
        from_ = mask_card(item.get("from")) + ' -> '
    else:
        from_ = ''

    to_ = mask_card(item.get("to"))

    return f'{item_date} {item.get("description")}\n' \
           f'{from_}{to_}\n' \
           f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n'



# 2019-08-26T10:50:58.294041 -> 26.08.2019
def format_date(str_date):
    '''берет строку даты до 10 символа, уберает пробелы и переворачивает дату'''
    list_date = str_date[:10].split('-')
    return '.'.join(reversed(list_date))


# Счет 64686473678894779589 -> Счет 64686473678 *** 9589
def mask_card(card):
    '''маскирует номер счета и номер карты по стандарту'''
    card = card.split(' ')
    if card[0] == 'Счет':
        return f'{card[0]} **{card[-1][-4:]}'
    return f'{" ".join(card[:-1])} {card[-1][:4]} {card[-1][4:6]}** **** {card[-1][-4:]}'


def main():
    data = load_data()
    data = filter_sort(data)

    for i in data:
        print(formatted_data(i))


if __name__ == '__main__':
    main()

