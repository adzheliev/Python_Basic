ip = input('Введите IP: ')

point = ip.count('.')

if point != 3:
    print('Адрес — это четыре числа, разделённые точками.')
else:
    iplist = ip.split('.')
    count = 0
    for i in iplist:
        if i.isdigit():
            if int(i) < 0:
                print(i,'меньше нуля')
                break
            elif int(i) > 255:
                print(i, 'превышает 255.')
                break
            else:
                count += 1
        else:
            print(i, '— это не целое число.')

    if count == 4:
        print('IP-адрес корректен.')

