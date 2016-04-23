# -*- coding: UTF-8 -*-
# Load Ngra text files into database
import sqlite3
import csv
conn = sqlite3.connect('Ngram.sqlite')
conn.text_factory = str
cur = conn.cursor()



def create_tables():
# Do some setup , configuration tables
    cur.executescript('''
    DROP TABLE IF EXISTS Qgram;
    DROP TABLE IF EXISTS Singlewords;
    DROP TABLE IF EXISTS Qfreq;

    CREATE TABLE Qgram (
        first   INTEGER,
        second INTEGER,
        third INTEGER,
        fourth INTEGER,
        freq INTEGER,
        PRIMARY KEY (first, second, third, fourth)
    );

    CREATE TABLE Singlewords (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        word  TEXT UNIQUE
    );

    CREATE TABLE Qfreq (
        qngram_id     INTEGER,
        word_id   INTEGER,
        freq        INTEGER,
        PRIMARY KEY (QNgram_id, word_id)
    )
    ''')


def load_single_words():

    with open('w4_.txt', 'r') as f:
        w4 = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)
        for row in w4:
            # row = row.strip().split()
            for word in row[1:5]:
                #print word
                cur.execute('''INSERT OR IGNORE INTO Singlewords (word)
                            VALUES ( ? )''', (word, ) )
        conn.commit()


def load_qgram():
    with open('w4_.txt', 'r') as f:
        w4 = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)
        # counter = 0
        for row in w4:
            # if counter > 100:
            #    break

            # row = row.strip().split()
            freq = row[0]
            word_id =[]
            # print freq
            for word in row[1:5]:
                # print word
                cur.execute('SELECT id FROM Singlewords WHERE word = ? ', (word, ))
                word_id.append(cur.fetchone()[0])
                # print word_id

            cur.execute('''INSERT or IGNORE INTO Qgram
                 (first, second, third, fourth, freq) VALUES ( ?, ?, ?, ?, ? )''',
                 (word_id[0], word_id[1], word_id[2], word_id[3], freq ) )
            # counter += 1
        conn.commit()

# main programme
create_tables()
load_single_words()
load_qgram()
conn.close()
