import random
import re

# Read in all the words in one go
with open("applications\markov\input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

    cache = {}
    words2 = words.split()
    for i in range(len(words2) - 1):

        if words2[i] not in cache:
            cache[words2[i]] = [words2[i+1]]
        else:
            cache[words2[i]].append(words2[i+1])

    # print(cache)
    capitalized_words = r"((?:[A-Z][a-z']+)+)"

    endingwords = r"(\w*\.|\w*\?|\w*\!)"

    # this is all the ending words
    end = re.findall(endingwords, words)

    # this is all the capitalized words
    cap = re.findall(capitalized_words, words)

    starter = random.choice(cap)

    sentence = starter

    print(starter)

    stop = False
    while stop == False:
        random_word = random.choice(cache[starter])

        if random_word in end:
            sentence += f' {random_word}'
            break
        else:
            sentence += f' {random_word}'
            starter = random_word
    print(sentence)
# TODO: construct 5 random sentences
# Your code here
