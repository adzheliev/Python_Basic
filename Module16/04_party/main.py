guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек: ', guests)
    choice = input('Гость пришёл или ушел? ')

    if choice == 'пришел':
        if len(guests) >= 6:
            name = input('Имя гостя: ')
            print('Прости', name, ',но мест нет')
        elif len(guests) < 6:
            name = input('Имя гостя: ')
            print('Привет', name, '!')
            guests.append(name)
    elif choice == 'ушел':
        name = input('Имя гостя: ')
        print('Пока', name, '!')
        guests.remove(name)
    elif choice == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break

