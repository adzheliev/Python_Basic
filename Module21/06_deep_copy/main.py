site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def phonesale(n, site):
    count = 0
    while count < n:
        phone = input('Введите название продукта для нового сайта: ')
        for key, value in site.items():
            if 'title' in key:
                value[key] = 'Куплю/продам ',phone, 'недорого'
            elif 'h2' in key:
                value[key] = 'У нас самая низкая цена на', phone
            return site
        else:

            for key, value in site.items():
                if type(value) == dict:
                    result = phonesale(n, value)
                    if result is not None:
                        return result


n = int(input('Сколько сайтов: '))

print(phonesale(n, site))