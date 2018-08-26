from tkinter import *
import sys
def display():

#takes string inside the widget
    s = e1.get()
    #print(s)
    #definition of alphabet
    alp = "abcdefghijklmnopqrstuvwxyz"

    f = open("encryption.txt",'w')
    alp_t = []
    #turning a string into an array
    for x in range(0, len(alp)):
        alp_t.append(alp[x])


    def printf(word):
        print(word)
        print("\n")
    #takes a string and turns it into an array
    word = s
    word_t = []
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
    #sys.exit()


def translate():
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


#calls canvas
master = Tk()
#labels some space on the widget
Label(master, text = "Encrypt your message").grid(row = 0)
#entry parameters
e1 = Entry(master)
e1.grid(row = 1, column = 0)
#creating buttons and assigning commands to them
Button(master,text="Quit",command = quit).grid(row=3,column=0,sticky=W,pady=4)
Button(master,text="Dispaly",command=display).grid(row=3, column=1, sticky=W,pady=4)
Button(master,text="Translate",command=translate).grid(row=3, column=2,sticky=W,pady=4)
#looping a master
mainloop()
