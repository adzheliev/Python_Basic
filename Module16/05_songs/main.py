violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

total = 0
number = int(input('Сколько песен выбрать? '))

for i in range (1, number + 1):
    print('Название ', i, '-й песни: ', end=' ')
    song = input()
    for l in violator_songs:
        if l[0] == song:
            total += l[1]

print('Общее время звучания песен: ', round(total, 2), 'минуты')




