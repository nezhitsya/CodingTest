data = input()
alphabet = []
num = 0

for x in data :
    if x.isalpha() :
        alphabet.append(x)
    else :
        num += int(x)

alphabet.sort()

if num != 0 :
    alphabet.append(str(num))

print(''.join(alphabet))