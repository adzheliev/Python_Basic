while True:
    password = input('Придумайте пароль: ')

    countnum = 0
    countbig = 0

    for i in password:
        if i.isupper():
            countbig += 1
        elif i.isdigit():
            countnum += 1

    if countbig < 1 or countnum < 3:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
