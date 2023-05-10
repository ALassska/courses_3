from func import format_date, mask_card, filter_sort, formatted_data, load_data


def test_format_date():
    assert format_date("2019-08-26T10:50:58.294041") == "26.08.2019"


def test_mask_card():
    assert mask_card("Maestro 1596837868705199") == 'Maestro 1596 83** **** 5199'
    assert mask_card('Счет 64686473678894779589') == 'Счет **9589'


def test_filter_sort():
    assert filter_sort([{
    "state": "EXECUTED",
    "date": "11"},
    {"state": "CANCELED",
    "date": "4"},
    {"state": "EXECUTED",
    "date": "50"},
    {"state": "EXECUTED",
     "date": "30"},
    {"state": "EXECUTED",
     "date": "23"},
    {"state": "EXECUTED",
     "date": "35"},
    {"state": "EXECUTED",
     "date": "76"}
    ]) == [{'state': 'EXECUTED', 'date': '76'}, {'state': 'EXECUTED', 'date': '50'}, {'state': 'EXECUTED', 'date': '35'}, {'state': 'EXECUTED', 'date': '30'}, {'state': 'EXECUTED', 'date': '23'}]


def test_load_data():
    result = load_data("../json_for_func_test.json")
    assert len(result) == 1

def test_formatted_data():
    assert formatted_data({
    "date": "2018-08-19T04:27:37.904916",
    "operationAmount": {
      "amount": "56883.54",
      "currency": {
        "name": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 6831982476737658",
    "to": "Visa Platinum 8990922113665229"
  }) == '19.08.2018 Перевод с карты на карту\n''Visa Classic 6831 98** **** 7658 -> Visa Platinum 8990 92** **** 5229\n''56883.54 USD\n\
'