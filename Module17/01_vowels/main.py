def analis(text):
    letters = "аеёиоуюя"
    l = [c for c in text if c in letters]
    print("Список гласных букв:", l)
    print("Длина списка:", len(l))


text = input("Введите текст: ")

analis(text)

