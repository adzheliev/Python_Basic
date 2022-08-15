message = input('Сообщение: ').split()

reversemessage = []

for word in message:
    if word[-1] == '.' or word[-1] == ',' or word[-1] =='!' or word[-1] =='?':
        word = word[::-1] + word[-1]
        word = word[1::]
        reversemessage.append(word)
    else:
        word = word[::-1]
        reversemessage.append(word)
a = ' '.join(reversemessage)

print('Новое сообщение: ', a)

