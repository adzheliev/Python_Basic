def item_checker(line):
    try:
        name, email, age = line.split()
    except IndexError:
        pass
    else:
        if not namecheck(name):
            raise NameError('Поле имени содержит НЕ только буквы')
        if not emailcheck(email):
            raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку)')
        if not agecheck(age):
            raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')


def namecheck(name):
    return name.isalpha()


def emailcheck(email):
    if '.' not in email and '@' not in email:
        return False
    else:
        return True


def agecheck(age):
    if not age.isnumeric() or (int(age) < 10 or int(age) > 99):
        return False
    else:
        return True


goodfile = open('registrations_good.log', 'a', encoding='utf-8')
badfile = open('registrations_bad.log', 'a', encoding='utf-8')


with open('registrations.txt', 'r', encoding='utf-8') as initial:
    for line in initial:
        try:
            string = item_checker(line)
        except IndexError:
            badfile.write(line + ' НЕ присутствуют все три поля: IndexError.' + '\n')
        except NameError:
            badfile.write(line + ' Поле имени содержит НЕ только буквы: NameError' + '\n')
        except SyntaxError:
            badfile.write(line + ' Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError' + '\n')
        except ValueError:
            badfile.write(line + ' Поле «Возраст» НЕ является числом от 10 до 99: ValueError' + '\n')
        else:
            goodfile.write(line + '\n')

goodfile.close()
badfile.close()