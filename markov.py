"""Generate Markov text from text files."""

import random

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path)

    lines_in_file = ""
    for line in file:
        line = line.rstrip()
        lines_in_file = lines_in_file + line + " "

    return lines_in_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    new_text = []
    new_text = text_string.split()

    chains = {}

    string_len = range(len(new_text) - 2)
    for l in string_len:
        key_dic = (new_text[l], new_text[l+1])
        #if item not in dictionary, add item
        if key_dic not in chains:
            chains[key_dic] = [new_text[l+2]]
        else:
            chains[key_dic].append(new_text[l+2])

    return chains


def make_text(chains):
    """Return text from chains."""
    words = []

    dict_keys = sorted(chains)
    first_words = random.choice(dict_keys)

    a, b = first_words
    words.append(a)
    words.append(b)

    #find value of tuple and add to words list
    next_word = random.choice(chains[first_words])
    words.append(next_word)

    #check to see if tuple is already a key in dictionary, if not - stop
    while True:
        new_tuple = tuple(words[-2:])

        if new_tuple not in dict_keys:
            break
            
        next_word = random.choice(chains[new_tuple])
        words.append(next_word)


    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

#print(chains)

print(random_text)

#print(input_text)
# make_text(input_text)