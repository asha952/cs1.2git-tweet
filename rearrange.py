import random
import sys

from python_quote import random_python_quote

sentence = random_python_quote()

'''wordsL = sentence.split()


for words in wordsL:
    print(words)
'''

words = sentence.split()
random.shuffle(words)
new_senten = ' '.join(words)

print(new_senten)

