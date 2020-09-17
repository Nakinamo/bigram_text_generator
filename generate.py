import random

next_word = {}
weight = {}

def choose(s):
    a = random.uniform(0, 1)
    i = 0
    while i + 1 < len(weight[s]) and weight[s][i] < a:
        a -= weight[s][i]
        i += 1
    return i

print('Enter the path to the model.')
f = open(input(), 'r')
model = f.read()
exec(model)
f.close()

print('Enter the random number generator seed.')
seed = int(input())
random.seed(seed)

print('Enter the supposed length of the text.')
lower_bound = int(input())

prev = '$'
word_count = 0

while True:
    word = next_word[prev][choose(prev)]
    if word == '$':
        if prev != '$':
            print('. ', end = '')
        if word_count >= lower_bound:
            break
    else:
        print(' ' + word if prev != '$' else word.title(), end = '')
        word_count += 1
    prev = word
print()
