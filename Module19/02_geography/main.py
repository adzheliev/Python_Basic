N = int(input('Количество стран: '))

countries = dict()

for i in range(1, N + 1):
    print(i,'-я страна: ', end='')
    country = input().split()
    for i in country[1:]:
        countries[i] = country[0]

for i in range(1, 4):
     print('Введите', i,'-й город: ', end='')
     city = input()
     if city in countries:
         print('Город', city, 'расположен в стране', countries.get(city))
     else:
         print('По городу', city, 'нет информации')


