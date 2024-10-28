from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)
words = ['nice', 'carrots','bananas']
anagrams = []
# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)

# use map function  map(function, data)
# print(list(map(jumble,words)))


# use  comprehension 
print([jumble(word) for word in words])