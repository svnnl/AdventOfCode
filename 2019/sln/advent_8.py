with open('../data/advent_8.txt') as f:
    data = list(f.read())

image = data[:25 * 6]

least = 1000000000
res = 0
while data:
    print(len(data))
    layer = data[:25 * 6]
    data = data[25 * 6:]

    i = layer.count('0')
    if i < least:
        least = i
        res = layer.count('1') * layer.count('2')

    s = ''
    for lc, ic in zip(layer, image):
        if ic == '2':
            s += lc
        else:
            s += ic
    image = s

print(res)

for i in range(6):
    print(image[i * 25:(i + 1) * 25].replace('0', ' '))
