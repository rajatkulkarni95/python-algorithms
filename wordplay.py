# A Wordplay with Vowels and Consonants

vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Enter a word to play : ')
vow_array = []
cons_array = []


def Wordplay(word):
    word_array = list(word)
    for x in vowels:
        if x in word_array:
            position = word_array.index(x)
            for i in range(position, len(word_array)):
                vow_array.append(word[position:position+i])

    for x in word_array:
        if x not in vowels:
            position = word_array.index(x)
            for i in range(position, len(word_array)):
                cons_array.append(word[position:position+i])


Wordplay(word)

if len(vow_array) > len(cons_array):
    print(
        f'A is the winner with {len(vow_array)} points. The list is {vow_array}')
else:
    print(
        f'B is the winner with {len(cons_array)} points. The list is {cons_array}')
