import re, text_cleanup, random

# Tuple (of word pair) to Dictionary (of appearances)
# Example: Key ("machine", "learning") -> Value {"to": 3.0, "from": 2.0}
raw_markov_mapping = {}

# Tuple (of word pair) to Dictionary (of flattened/normalized appearances)
# Example: Key ("machine", "learning") -> Value {"to": 0.6, "form": 0.4}
norm_markov_mapping = {}

# Set of start points for random walks
starts = []

# Created Variable: Run markov map creation once
created_markov = False

# Change List to Tuple for raw_mapping's key generation
def toTupleHashKey(lst):
    return tuple(lst)

def addItemToRawMapping(history, word):
    global raw_markov_mapping

    # Register the entirety of history into the mapping
    while len(history) > 0:
        first = toTupleHashKey(history)
        # If key already exists in raw mapping
        if first in raw_markov_mapping:
            # If key value pair exists in raw mapping, iterate count appearance
            if word in raw_markov_mapping[first]:
                raw_markov_mapping[first][word] += 1.0
            else:
                raw_markov_mapping[first][word] = 1.0
        else:
            # 'first' word not registered in markov map, create new object reference
            raw_markov_mapping[first] = {}
            raw_markov_mapping[first][word] = 1.0
        history = history[1:]

# Construct and Normalized Markov Map
def constructRawMarkovMap(corpus, markov_gram_length):
    global raw_markov_mapping

    # Create raw markov map out of corpus itself
    starts.append(corpus[0])
    for i in range(1, len(corpus) - 1):
        if i <= markov_gram_length:
            history = corpus[:(i+1)]
        else:
            history = corpus[(i-markov_gram_length+1):i+1]
        follow = corpus[i+1]
        if history[-1] == "." and follow not in ".,!?;":
            starts.append(follow)
        addItemToRawMapping(history, follow)

def constructNormMarkovMap():
    global raw_markov_mapping
    global norm_markov_mapping
    # Normalization, then place key, value pairs into normalized markov mapping
    for key, value in raw_markov_mapping.items():
        total = sum(value.values())
        norm_markov_mapping[key] = dict([(k, v/total) for k, v in value.items()])

def nextWord(prevList):
    total = 0.0
    return_val = ""
    index = random.random()
    # Reduce prevList values until it is a key in the markov map
    while toTupleHashKey(prevList) not in norm_markov_mapping:
        if prevList:
            prevList.pop(0)
        else:
            prevList = random.choice(starts).capitalize()
    # Given the prevList, get random word from mapping that follows criteria
    for key, value in norm_markov_mapping[toTupleHashKey(prevList)].items():
        total += value
        if total >= index and return_val == "":
            return_val = key
    return return_val

def generateSentence(markov_gram_length):
    curr = random.choice(starts)
    # print("Random Start: " + curr)
    sent = curr.capitalize()
    prevList = [curr]
    # Continue to add words until 'word w/ period' aka terminating markov node reached
    while (curr not in "."):
        # print("Inside while loop " + str(prevList))
        # Generate next word in sentence, then append it to list
        curr = nextWord(prevList)
        prevList.append(curr)
        # Sentence longer than what user wanted
        if (len(prevList) > markov_gram_length):
            prevList.pop(0)
        if (curr not in ".,!?;"):
            sent += " " # Spaces between words, not between punctuation
        sent += curr
    return sent

def printRawMarkov():
    global raw_markov_mapping
    for key, value in raw_markov_mapping.items():
        print(key, value)

def printNormMarkov():
    global norm_markov_mapping
    for key, value in norm_markov_mapping.items():
        print(key, value)

def run():
    global created_markov
    if not created_markov:
        corpus = text_cleanup.create_word_list('book_sample.txt')
        # Larger markov gram lengths take longer to run, but generate more logical sentences
        constructRawMarkovMap(corpus, 6)
        constructNormMarkovMap()
        created_markov = True

    sentence = generateSentence(6)
    while (len(sentence.split()) < 7 or len(sentence) > 140):
        sentence = generateSentence(6)
    return sentence

if __name__ == '__main__':
    print(run())
