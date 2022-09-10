initial = open('text.txt', 'r')
file = open('cipher_text.txt', 'a')
upperletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerletters = 'abcdefghijklmnopqrstuvwxyz'

step = 1
for line in initial:
    for sym in line:
        if sym in upperletters:
            symindex = upperletters.index(sym)
            codedsym = upperletters[symindex + step]
            file.write(codedsym)
        elif sym in lowerletters:
            symindex = lowerletters.index(sym)
            codedsym = lowerletters[symindex + step]
            file.write(codedsym)
    step += 1
    file.write('\n')

initial.close()
file.close()
