nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
new = [y for x in nice_list for y in x]
new2 = [y for x in new for y in x]

print('Ответ: ', new2)

