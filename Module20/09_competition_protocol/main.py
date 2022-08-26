N = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
partecipants = {}
for i in range(1, N + 1):
    print(i,'-я запись: ', end='')
    score, name = input().split()
    score = int(score)
    if name in partecipants:
        if score > partecipants[name]:
            partecipants[name] = score
    else:
        partecipants[name] = score
partecipants = list(partecipants.items())
print(partecipants)

partecipants.sort(key=score)
print(partecipants)