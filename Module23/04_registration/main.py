def checkallfields(splitedline):
    if len(splitedline) != 3:
        return False
    else:
        return True


def namecheck(splitedline):
    if not splitedline[0].isalpha():
        return False
    else:
        return True


def emailcheck(splitedline):
    if '.' not in splitedline[1] and '@' not in splitedline[2]:
        return False
    else:
        return True


def agecheck(splitedline):
    if not splitedline[2].isnumeric() or (int(splitedline[2]) < 10 or int(splitedline[2]) > 99):
        return False
    else:
        return True


goodfile = open('registrations_good.log', 'a', encoding='utf-8')
badfile = open('registrations_bad.log', 'a', encoding='utf-8')

flag1 = flag2 = flag3 = flag4 = False
with open('registrations.txt', 'r', encoding='utf-8') as initial:
    for line in initial:
        splitedline = line.split()
        if checkallfields(splitedline) == False:
            badfile.write(' '.join(splitedline) + ' НЕ присутствуют все три поля: IndexError.')
            badfile.write('\n')
        else:
            flag1 = True
            if namecheck(splitedline) == False:
                badfile.write(' '.join(splitedline) + ' Поле имени содержит НЕ только буквы: NameError.')
                badfile.write('\n')
            else:
                flag2 = True

            if emailcheck(splitedline) == False:
                badfile.write(' '.join(splitedline) + ' Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError.')
                badfile.write('\n')
            else:
                flag3 = True

            if agecheck(splitedline) == False:
                badfile.write(' '.join(splitedline) + ' Поле «Возраст» НЕ является числом от 10 до 99: ValueError.')
                badfile.write('\n')
            else:
                flag4 = True

            if flag1 == True and flag2 == True and flag3 == True and flag4 == True:
                goodfile.write(' '.join(splitedline))
                goodfile.write('\n')

goodfile.close()
badfile.close()