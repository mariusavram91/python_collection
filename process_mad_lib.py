#!/usr/bin/python3

# Let's put it all together. Write code for the function process_madlib, which
# takes in a string "madlib" and returns the string "processed", where each
# instance of "NOUN" is replaced with a random noun and each instance of "VERB"
# is replaced with a random verb. You're free to change what the random
# functions return as verbs or nouns for your own fun, but for submissions keep
# the code the way it is!

from random import randint


def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"


def random_noun():
    random_num = randint(0, 1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"


def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]


def process_madlib(mad_lib):
    processed = ""
    sentence_len = len(mad_lib)
    char_position = 0
    substring_len = 4
    while char_position < sentence_len:
        processed_word = word_transformer(
            mad_lib[char_position:char_position + substring_len])
        processed += processed_word
        if len(processed_word) > 1:
            char_position += substring_len
        else:
            char_position += 1
    return processed

test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print(process_madlib(test_string_1))
print(process_madlib(test_string_2))
