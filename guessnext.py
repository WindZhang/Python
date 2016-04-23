# Guess next word based on the input
# search the database

import sqlite3
import re
from tkinter import *
conn = sqlite3.connect('Ngram.sqlite')
cur = conn.cursor()

PROGRAM_NAME = "Guess the next word"

a2z = 'abcdefghijklmnopqrstuvwxyz'

# helper functions

# fetch single word by id

def id_to_word (word_id):
    cur.execute('SELECT word FROM COCA WHERE id = ?' , (word_id,))
    try:
        nextword = cur.fetchone()[0]
        return nextword
    except:
        print ('not found id_to_word')


# match the id by given single word

def word_to_id (word):
    cur.execute('SELECT id  FROM COCA WHERE word = ?',(word,))
    try:
        word_id =cur.fetchone()[0]
        return word_id
    except:
        print ('not found word_to_id ')

# retrive the second word based on 'first' word's ID
# lookup in Bgram table

def retrive_second_word(first):
    cur.execute('''
                SELECT second FROM Bgram WHERE first = ?
                             ORDER BY freq DESC LIMIT 10''',(first[0],))
    try:
        second = cur.fetchall()
        return second
    except:
        return back_off_bgram(my_string.get())

# retrive the third word based on 'first, second' words'ID
# lookup in Tgram table
def retrive_third_word(first_second):
    cur.execute('''
                SELECT third FROM Tgram WHERE first = ? and second = ?
                             ORDER BY freq DESC LIMIT 10''',
                             (first_second[0],
                                first_second[1]))
    try:
        third = cur.fetchall()
        return third
    except:
        return back_off_bgram(my_string.get())


# retrive the fouth word based on 'first, second, third' words'ID
# lookup in Qgram table

def retrive_fourth_word(first_second_third):
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
        return back_off_bgram(my_string.get())


def retrive_fifth_word(first_second_third_fourth):
    cur.execute('''
                SELECT fifth FROM Fgram
                       WHERE first = ? and second = ? and third = ? and fourth = ?
                       ORDER BY freq DESC LIMIT 10''',
                (first_second_third_fourth[0],
                    first_second_third_fourth[1],
                       first_second_third_fourth[2],
                          first_second_third_fourth[3])
                )
    try:
        fifth = cur.fetchall()
        return fifth
    except:
        return back_off_bgram(my_string.get())


def phrase_to_id(phrase):
    return [word_to_id(i) for i in phrase.split()]

# If not found in current gram , using back_off method
def back_off_bgram(inputed):
    last_word = (inputed.split()[-1])
    gram_key = phrase_to_id(last_word)
    n = retrive_second_word(gram_key)
    return(n)


def guess():
        n = ['1','3','4', '5', '7'] # predicit auto-complete
        inputed = my_string.get()
        print (inputed, len(inputed))
        if inputed[-1] in a2z and ' ' not in inputed and not inputed.endswith(' '):
            pass
        else:
            gram_key = phrase_to_id(inputed)
            if len(gram_key) == 0:
                n = ['1','3','4', '5', '7'] # predicit auto-complete
            elif len(gram_key) == 1:
                n = retrive_second_word(gram_key)
            elif len(gram_key) == 2:
                n = retrive_third_word(gram_key)
            elif len(gram_key) == 3:
                n = retrive_fourth_word(gram_key)
            elif len(gram_key) == 4:
                n = retrive_fifth_word(gram_key)
            else:
                n = back_off_bgram(inputed)
        next_word =[id_to_word(i[0]) for i in n]
        guess_result.set (', '.join(next_word))


def words_so_far(event):
    guess()

root = Tk()
root.geometry('350x350')
root.title(PROGRAM_NAME)

global my_string
global guess_result
my_string = StringVar()
guess_result = StringVar()


Label(text="Type words here").pack()
entry = Entry(root,width=40,  textvariable =my_string)
entry.pack()
my_string.set(' ')
entry.bind("<Any-KeyPress>", words_so_far)


Label(text="Hints", fg = 'Blue').pack()
result = Entry(root, textvariable=guess_result, width = 40, fg = 'Blue').pack()


root.mainloop()
conn.close()
