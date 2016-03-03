import collections

f = raw_input('filename [words.txt]:') or 'words.txt'

def most_frequent(string):
    """
    1. Build a list of tuples with character frequency as sort key. 
    2. (reverse) sort the list
    3. Extract characters and frequency % sorted in decreasing order
    """
    char_freq = []
    freq_dict = collections.Counter(string)
    for key, val in freq_dict.items():
        char_freq.append((val, key))
    numofchars = sum(freq_dict.values())

    char_freq.sort(reverse=True)

    decrease_char_freq = []
    for freq, char in char_freq:
        decrease_char_freq.append((round((float(freq) / numofchars), 4) * 100, char))

    return decrease_char_freq

def make_string(f):
    o = open(f, 'r')
    raw_string = o.read()
    string = raw_string.translate(None, '\n\r')
    o.close()
    return string

if __name__ == '__main__':
    for freq, char in most_frequent(make_string(f)):
        print char, ':', freq, '%'

