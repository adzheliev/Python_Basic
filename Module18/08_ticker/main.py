string1 = input('Первая строка: ')
string2 = input('Вторая строка: ')

if len(string1) != len(string2):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    count = 1
    for i in range(len(string1)):
        string2 = string2[-1] + string2[:-1]
        if string2 == string1:
            print('Первая строка получается из второй со сдвигом', count)
        else:
            count += 1

    if count > len(string1):
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')






