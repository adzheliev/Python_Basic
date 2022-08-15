file_name = input('Название файла: ')
check = '@№$%^&*().'

if file_name[0] in check:
    print('Ошибка: название начинается на один из специальных символов.')
elif not file_name.endswith(('.txt', '.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')