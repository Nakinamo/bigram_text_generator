import os

print('Enter the path to the corpus.')
f = open(input(), 'r')
text = f.read()
text = text.lower()
f.close()

specials = '~`!?@#$%^&*"()_+-=\\/,;:[]{}'
for i in specials:
    text = text.replace(i, ' ')
text = text.replace('.', ' $ ')
text = text.replace('\'', '\\'+'\'')

freq = {}
previous = '$'
for word in text.split():
    if (previous, word) in freq:
        freq[(previous, word)] += 1
    else:
        freq[(previous, word)] = 1
    previous = word

model = {}

for pair in freq:
    if not pair[0] in model:
        model[pair[0]] = set()
    model[pair[0]].add((pair[1], freq[pair]))

next_word = {}
weight = {}

f = open('tmp.txt', 'w+')
text = ''
for i in model:
    next_word[i] = []
    weight[i] = []
    count = 0
    for j in model[i]:
        next_word[i].append(j[0])
        weight[i].append(j[1])
        count += j[1]
    for j in range(len(weight[i])):
        weight[i][j] /= count
    print(f'next_word[\'{i}\'] =', next_word[i], f'\nweight[\'{i}\'] =', weight[i], file = f)

f = open('tmp.txt', 'r')
text = f.read()
text = text.replace('\\\\', '\\')
f = open('model.txt', 'w')
os.remove('tmp.txt')
f.truncate()
print(text, file = f)
f.close()

