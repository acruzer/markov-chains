"""Generate Markov text from text files."""

from random import choice

from sys import argv

n = choice(range(2,10))

print("n is... \n")
print(n)


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()

    return contents


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
    new_text = text_string.split()

    chains = {}

    string_len = range(len(new_text) - n)

    for l in string_len:
        #for every number in n, add the 
        key_dic = tuple(new_text[l:l+n])
        #if item not in dictionary, add item
        if key_dic not in chains:
            chains[key_dic] = [new_text[l+n]]
        else:
            chains[key_dic].append(new_text[l+n])


    return chains


def make_text(chains):
    """Return text from chains."""
    words = []
    caps_keys = []

    #if first value of dict_leys is capitalized, start words, else skip
    dict_keys = sorted(chains)


    for k in dict_keys: 
        if k[0].islower() == False:
            caps_keys.append(k)
    

    first_words = choice(caps_keys)

    #find value of tuple and add to words list
    words = list(first_words)
    next_word = choice(chains[first_words])
    words.append(next_word)


    #check to see if tuple is already a key in dictionary, if not - stop
    while True:
        new_tuple = tuple(words[-n:])

        if new_tuple not in dict_keys:
            break
            
        next_word = choice(chains[new_tuple])
        words.append(next_word)


    return " ".join(words)


input_path = argv[1]

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