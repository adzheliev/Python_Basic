def sum(*args):
    total = 0
    for element in args:
        if isinstance(element, int):
            total += element
        else:
            total += sum(element)

        return total

print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))
