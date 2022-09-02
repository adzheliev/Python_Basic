def sum(*args):
    if type(args) == tuple:
        total = 0
        for i in args:
            total += i
        return total

    elif type(args) == list:
        total = 0
        for subelement in args:
            if type(subelement) == int:
                total = total + subelement
            elif type(subelement) == list:
                sum(subelement)
        return total

print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))
