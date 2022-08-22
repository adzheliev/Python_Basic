goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for i_goods in goods:
    total = 0
    total_quantity = 0
    for i_store in store[goods[i_goods]]:
        summitem = i_store['price'] * i_store['quantity']
        total_quantity += i_store['quantity']
        total += summitem
    print(i_goods,' - ', total_quantity, 'штук, стоимость', total, 'рубля')



