nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new = [i for i in nice_list for i in i for i in i]

print('Ответ: ', new)

