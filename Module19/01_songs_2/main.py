violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songsnumber = int(input('Сколько песен выбрать? '))
totaltime = 0

for i in range(1, songsnumber + 1):
    print('Введите название',i,'-й песни: ', end='')
    song = input()
    if violator_songs.get(song):
        totaltime += violator_songs.get(song)
    else:
        print('Такой песни нет в списке')

print('Общее время звучания песен: ',round(totaltime, 2))