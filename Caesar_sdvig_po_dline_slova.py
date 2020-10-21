eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = input()

def word_caesar(word):
    caesar_step = 0
    for i in range(int(len(word))):
        if word[i].isalpha():
            caesar_step += 1

    for i in range(int(len(word))):
        if word[i] in eng_upper_alphabet:
            print(eng_upper_alphabet[(eng_upper_alphabet.find(word[i]) + caesar_step) % len(eng_upper_alphabet)], end='')
        elif word[i] in eng_lower_alphabet:
            print(eng_lower_alphabet[(eng_lower_alphabet.find(word[i]) + caesar_step) % len(eng_lower_alphabet)], end='')
        else:
            print(word[i], end='')
    print(' ',end='')
mlist = text.split()
for i in mlist:
    word_caesar(i)

