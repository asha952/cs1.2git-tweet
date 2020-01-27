import random
f = open('listOfWords.txt', 'r')

lines = [line.rstrip('\n') for line in f]

"""for lines in f:"""
print(lines)
print("-----------")

"""print(random.choice(lines))
print("-----------")
"""

"""total_words = input("give a number 1-10: ")"""
"""sentence = "j " """

sentence = " ".join(lines)
print(sentence)

"""while it < total_words:"""

"""print(random.sample(words, 3))"""

"""val = input("input a number from 1-10")"""


"""def random_sentence():
    '''for x in val'''
    print(random.choice(1, (len(words)) - 1))
"""

f.close()
