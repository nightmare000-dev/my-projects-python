dict = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 4,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10
}

first = input('Player 1: ').lower()
second = input('Player 2: ').lower()

cnt_first = 0
cnt_second = 0

for i in first:
    for j in dict:
        if i in dict: cnt_first += dict[j]

for i in second:
    for j in dict:
        if i in dict: cnt_second += dict[j]

if cnt_first > cnt_second: print('Player 1 wins!')
elif cnt_second > cnt_first: print('Player 2 wins!')
else: print('Tie!')       