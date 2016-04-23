# Guess next word based on the input
# search the database

import sqlite3
from tkinter import *
conn = sqlite3.connect('Ngram.sqlite')
cur = conn.cursor()
conn.text_factory = str

PROGRAM_NAME = "Guess next word"

root = Tk()
root.geometry('350x350')
root.title(PROGRAM_NAME)

# helper functions

# fetch single word by id

def id_to_word (word_id):
    cur.execute('SELECT word FROM Singlewords WHERE id = ?' , (word_id,))
    try:
        nextword = cur.fetchone()[0]
        return nextword
    except:
        print ('not found')


# match the id by given single word

def word_to_id (word):
    cur.execute('SELECT id  FROM Singlewords WHERE word = ?',(word,))
    try:
        word_id =cur.fetchone()[0]
        return word_id
    except:
        print ('not found')


# retrive the third word based on 'first, second' words'ID
# lookup in Tgram table
def retrive_third_word(first_second):
    pass


# retrive the second word based on 'first' word's ID
# lookup in Bgram table

def retrive_second_word(first):
    pass


# retrive the fouth word based on 'first, second, third' words'ID
# lookup in Qgram table

def retrive_fouth_word(first_second_third):
    cur.execute('''
                SELECT fourth FROM Qgram WHERE first = ? and second = ? and third = ?
                                       ORDER BY freq DESC LIMIT 10''',
                (first_second_third[0],
                    first_second_third[1],
                       first_second_third[2]) )
    try:
        fourth = cur.fetchall()
        return fourth
    except:
        print ('not found')


def phrase_to_id(phrase):
    return [word_to_id(i) for i in phrase.split()]

# predifine SELECT

def your_input():
    while True:
        # one_two_three =[]
        you_input = raw_input('Enter the text:')
        if you_input == 'done':
            break
        try:
            return phrase_to_id(you_input)
        except:
            continue


# main programme


# print your_input()

global my_string
global guess_result
global result
my_string = StringVar()
guess_result = StringVar()



def guess():
    inputed = my_string.get()
    qgram_key = phrase_to_id(inputed)
    # print(qgram_key)
    fouth = retrive_fouth_word(qgram_key)
    next_word =[id_to_word(i[0]) for i in fouth]

    guess_result.set (', '.join(next_word))

    # result(root, textvariable=guess_result, width = 40, justify=LEFT)
    # print (guess_result.get())


def how_many_words_so_far(event):
    # print (my_string.get())
    if len(my_string.get().split())==3:
        guess()
    else:
        pass

def callback(event): ##(2)
    print(dir(event))##(3) Inspecting the instance event
    print("you clicked at", event.x, event.y )##(4)


# frame = Frame(root, bg='khaki', width=130, height=80)
# frame.bind("<Control-s>", how_many_words_so_far)##(1)
# frame.pack()
# Label(text="guess results").pack()
# frame = Frame(root, bg='khaki', width=130, height=80).pack()
# result = Entry(root, textvariable=guess_result, width = 40, fg = 'Blue').pack

Label(text="Type words here").pack()
entry = Entry(root,width=40,  textvariable =my_string)
entry.bind("<Any-KeyPress>", how_many_words_so_far)
entry.pack()

Label(text="Hints", fg = 'Blue').pack()
# frame = Frame(root, bg='khaki', width=130, height=80).pack()
result = Entry(root, textvariable=guess_result, width = 40, fg = 'Blue').pack()
# frame.bind("<Button-1>", how_many_words_so_far)##(1)
# frame.pack()
# button_login = Button(root, text="Guess", command = how_many_words_so_far).pack()


root.mainloop()


# print (inputed)
# which_ngram = len(inputed)
# if which_ngram == 1:
#     retrive_second_word(inputed)
# elif which_ngram == 2:
#     retrive_third_word(inputed)
# elif which_ngram == 3:
#     retrive_fouth_word(inputed)
# else:
#     pass



# print word_to_id('child')
# print id_to_word(11594)
# print retrive_fouth_word(1,18,19)

conn.close()
