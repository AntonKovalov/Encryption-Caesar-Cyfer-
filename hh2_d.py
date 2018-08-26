#same as encryption
alp = "abcdefghijklmnopqrstuvwxyz"

f = open("encryption.txt",'r')
alp_t = []

for x in range(0, len(alp)):
    alp_t.append(alp[x])

def printf(word):
    print(word)
    print("\n")
#reading encrypted version from
#the file
word = f.read()
print(word)
word_t = []
for x in range(0, len(word)):
    word_t.append(word[x])

def crypt(word):
    for i in range(0,len(word)):
        up = word[i]
        word[i] = word[i].lower()
        if word[i] == (" " or "," or "." or "'"
        or ":" or ";" or "\"" or "!" or "?"):
            continue
        for j in range(0,len(alp_t)):
            if word[i] == alp_t[j]:
#slightly different algorythm for
#decryption, logic is the same
#array has to be circul
                if j < 2:
                     k = j + 23
                     if word[i] == up:
                         word[i] = alp_t[k]
                     else:
                         word[i] = alp_t[k].upper()

                else:
                    k = j - 3
                    if word[i] == up:
                       word[i] = alp_t[k]
                    else:
                       word[i] = alp_t[k].upper()

                break
crypt(word_t)
word = ''.join(word_t)
printf(word)
f.close()
