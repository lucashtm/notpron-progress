import string
import sys

alph = string.ascii_lowercase[:26]
word = sys.argv[1].lower()
direction = sys.argv[2].lower()

if direction == 'left':
    inc = -1
elif direction == 'right':
    inc = 1


shifted = []
for c in word:
    i = alph.find(c)
    if i >= 0:
        shifted.append(alph[i+inc])
    else:
        shifted.append(c)
print(''.join(shifted))
