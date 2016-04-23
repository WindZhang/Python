# /usr/bin/python3
# Load Ngra text files into database
import sqlite3
# import csv
import sys

global ENCODING
ENCODING ='latin-1'
conn = sqlite3.connect('Ngram.sqlite')
# conn.text_factory = str
cur = conn.cursor()

def validate_input():
    if len(sys.argv) < 2:
        print ('Uasge: python3 <laod_english.py> <input>')
        sys.exit()
    else:
        try:
            with open(sys.argv[1], 'r')  as f_in:
                pass
        except:
                print(sys.argv[1], ': File not found')
                sys.exit()


def create_tables():
# Do some setup , configuration tables
    cur.executescript('''
    CREATE TABLE COCA (
        ID INTEGER PRIMARY KEY,
        word  TEXT UNIQUE
    )
    ''')


def english_words():
    with open(sys.argv[1], 'r', encoding = ENCODING) as f:
        # corpus = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)
        for line in f:
            row = line.strip().split()
            for word in row[1:]:
                #print word
                cur.execute('''INSERT OR IGNORE INTO COCA (word)
                            VALUES ( ? )''', (word, ) )
        conn.commit()


def run():
    validate_input()
    # create_tables()
    english_words()
    conn.close()

run()
