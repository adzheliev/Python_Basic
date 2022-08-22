N = int(input('Введите количество заказов: '))

klient = dict()
klient_dict = dict()
for i in range(1, N +1):
    print(i,'-й заказ: ',end='')
    order = input().split()
    klient['name'] = order[0]
    klient['pizza'] = order[1]
    klient['quantity'] = order[2]
    klient_dict[i] = klient

print(klient_dict)

#for i in klientkeyssorted:
#    if i in klient:
#        print(i)
