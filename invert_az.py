import string
import sys

alph = string.ascii_lowercase[:26]
word = sys.argv[1].lower()
inverted = []
for c in word:
    i = alph.find(c)
    if i >= 0:
        inverted.append(alph[len(alph)-1-i])
print(''.join(inverted))