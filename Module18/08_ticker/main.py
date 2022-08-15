string1 = input('Первая строка: ')
string2 = input('Вторая строка: ')

if len(string1) != len(string2):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    list1 = list(string1)
    list2 = list(string2)
    count = 0
    for i in range(len(string1)):
        if list1 == list2:
            print('Первая строка получается из второй со сдвигом', count)
            break
        else:
            list1.insert(0, list1[-1])
            list1.pop(-1)
            count += 1
            if list1 == list2:
                print('Первая строка получается из второй со сдвигом', count)
                break
            elif count == len(string1):
                print('Первую строку нельзя получить из второй с помощью циклического сдвига.')





