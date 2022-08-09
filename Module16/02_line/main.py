class1 =[]
class2 = []

for i in range(160, 177, 2):
    class1.append(i)

for i in range (162, 181, 3):
    class2.append(i)

class1.extend(class2)
class1.sort()

print('Отсортированный список учеников: ', class1)