#definition of alphabet
alp = "abcdefghijklmnopqrstuvwxyz"

f = open("encryption.txt",'w')
d = open("input.txt","r")
alp_t = []
#turning a string into an array
for x in range(0, len(alp)):
    alp_t.append(alp[x])


def printf(word):
    print(word)
    print("\n")
#takes a string and turns it into an array
word = d.read()
word_t = []
d.close()
for x in range(0, len(word)):
    word_t.append(word[x])

#encryption algorythm
#takes a character in a string
#and searches for the same charcter in the alphabet
#after matching turns current character
#in the one 3 steps apart
def crypt(word):
    for i in range(0,len(word)):
# a variable to check uppercase letters
        up = word[i]
        word[i] = word[i].lower()
# checking other characters but letters
        if word[i] == (" " or "," or "." or "'"
        or ":" or ";" or "\"" or "!" or "?"):
            continue
        for j in range(0,len(alp_t)):
            if word[i] == alp_t[j]:
#array has to be circular
                if j > 22:
                     k = j - 23
#comparison to do uppercase letters
                     if word[i] == up:
                         word[i] = alp_t[k]
                     else:
                         word[i] = alp_t[k].upper()
                else:
                    k = j + 3
                    if word[i] == up:
                        word[i] = alp_t[k]
                    else:
                        word[i] = alp_t[k].upper()

                break
crypt(word_t)
#turning an array back into a string
word = ''.join(word_t)
printf(word)
#returning it to a file for further decryption
f.write(word)
f.close()
