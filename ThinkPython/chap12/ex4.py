from collections import OrderedDict

f = raw_input('filename [words.txt]:') or 'words.txt'

#def is_anagram(ref, word):
#    """
#    1. Take two words one being the reference.
#    2. Return True if the two are anagrams.
#    """
#    ref_to_list = list(ref)
#    word_to_list = list(word)
#    ref_sort = ref_to_list.sort()
#    word_sort = word_to_list.sort()
#    if ref_sort is word_sort:
#        return True

def list_words(f):
    """
    1. Take a text file and extract all the words separated by space and new line characters.
    2. Remove special characters.
    3. Return a list of words
    """
    word_list = []
    o = open(f)
    for word in o:
        word_list.append(word.strip('\n\r'))
    o.close()
    return word_list

def make_anagrams_dict(l):
    """
    1. Create a reference set of characters out of each item from a list of words.
    2. Search list of words for reference anagrams.
    3. Return a dictionary with references as keys and a list of their anagrams as values.
    """
    anagrams_dict_raw = {}
    anagrams_dict = {}
    for word in l:
        word_to_list = list(word)
        word_to_list.sort()
        ref = tuple(word_to_list)
        if ref not in anagrams_dict_raw:
            anagrams_dict_raw[ref] = [word]
        else:
            anagrams_dict_raw[ref].append(word)
    for key in anagrams_dict_raw:
        if len(anagrams_dict_raw[key]) >= 2:
            anagrams_dict[key] = anagrams_dict_raw[key]
    return anagrams_dict

def sort_anagrams_dict(d):
    return OrderedDict(sorted(d.items(), key=lambda t: len(t[1]), reverse=True))
     

if __name__ == '__main__':
    anagrams_dict = make_anagrams_dict(list_words(f))
#    for ref, words in make_anagrams_dict(list_words(f)).items():
#        print ref, ':', words
    for ref, words in sort_anagrams_dict(anagrams_dict).items():
        print ref, ':', words

