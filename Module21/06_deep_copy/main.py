from pprint import pprint
import copy

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
pprint(site)

def phonesale(n, site):
    copysite = copy.deepcopy(site)
    count = 0
    while count < n:
        phone = input('Введите название продукта для нового сайта: ')
        for key, value in copysite.items():
            if 'title' in key:
                value[key] = 'Куплю/продам ',phone, 'недорого'
            if 'h2' in key:
                value[key] = 'У нас самая низкая цена на', phone
            return copysite
        else:
            for key, value in copy.items():
                if type(value) == dict:
                    result = phonesale(n, value)
                    if result is not None:
                        return result

n = int(input('Сколько сайтов: '))

print(phonesale(n, site))