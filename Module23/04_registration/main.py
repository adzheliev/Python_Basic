def check(line):
    goodfile = open('registrations_good.log', 'a', encoding='utf-8')
    badfile = open('registrations_bad.log', 'a', encoding='utf-8')
    try:
        name, email, age = line.split()
    except:
        raise IndexError('НЕ присутствуют все три поля')
    finally:
        badfile.write(line)
    if not name.isalpha():
        raise NameError('Поле имени содержит НЕ только буквы')
        badfile.write(line)
    elif '.' not in email and '@' not in email:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку)')
        badfile.write(line)
    elif not age.isnumeric() or (int(age) < 10 or int(age) > 99):
        raise ValueError ('Поле «Возраст» НЕ является числом от 10 до 99')
        badfile.write(line)
    else:
        goodfile.write(line)
    goodfile.close()
    badfile.close()


with open('registrations.txt', 'r', encoding='utf-8') as initial:
    for line in initial:
        check(line)

