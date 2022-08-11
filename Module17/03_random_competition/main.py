import random

squad1 = [round(random.uniform(5, 10), 2) for i in range (20)]
squad2 = [round(random.uniform(5, 10), 2) for i in range (20)]
win = [max(squad1[i], squad2[i]) for i in range(20)]
print('Первая команда: ', squad1)
print('Вторая команда: ', squad2)
print('Победители тура:', win)