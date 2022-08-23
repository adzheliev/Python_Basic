N = int(input('Введите количество заказов: '))

client_dict = dict()

for i in range(1, N +1):
    buyer_name, pizza_name, pizza_cnt = input(str(i) + ' заказ: ').split()
    pizza_cnt = int(pizza_cnt)
    if buyer_name not in client_dict:
        client_dict[buyer_name] = {pizza_name: pizza_cnt}
    else:
        if pizza_name not in client_dict[buyer_name]:
            client_dict[buyer_name][pizza_name] = pizza_cnt
        else:
            client_dict[buyer_name][pizza_name] += pizza_cnt


for buyer_name, pizza_name in sorted(client_dict.items()):
    print(f'{buyer_name}:')
    for pizza_name, pizza_cnt in sorted(pizza_name.items()):
        print('     ', pizza_name, pizza_cnt)



