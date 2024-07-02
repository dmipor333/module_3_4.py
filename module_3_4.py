def single_root_worlds(root_word, *other_word):
    same_words = []
    root_word = root_word.lower()
    other_word = ''.join(other_word)
    other_word = other_word.lower()
    for i in other_word:
        if root_word in i or i in root_word:
            #same_words = other_word.count(root_word)
            #same_words += other_word
            same_words.append(i)
        #print(same_words)
    return same_words
result1 = single_root_worlds('kora', 'Koran', 'koRAN', 'korm')
result2 = single_root_worlds('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)