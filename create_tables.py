# database setup

import sqlite3
import csv
conn = sqlite3.connect('Ngram.sqlite')
# conn.text_factory = str
cur = conn.cursor()

def create_tables():
# Do some setup , configuration tables
# COCA as Corpus of American English Unigram
# Bgram as Bi-grams
# Tgram as Tri-grams
# Qgram as Four-grams
# Fgram as Five-grams

    cur.executescript('''
    DROP TABLE IF EXISTS COCA;
    DROP TABLE IF EXISTS Bgram;
    DROP TABLE IF EXISTS Tgram;
    DROP TABLE IF EXISTS Qgram;
    DROP TABLE IF EXISTS Fgram;

    CREATE TABLE COCA (
        id     INTEGER NOT NULL PRIMARY KEY,
        word  TEXT UNIQUE
    );

    CREATE TABLE Bgram (
        first   INTEGER,
        second INTEGER,
        freq INTEGER,
        PRIMARY KEY (first, second)
    );

    CREATE TABLE Tgram (
        first   INTEGER,
        second INTEGER,
        third INTEGER,
        freq INTEGER,
        PRIMARY KEY (first, second, third)
    );

    CREATE TABLE Qgram (
        first   INTEGER,
        second INTEGER,
        third INTEGER,
        fourth INTEGER,
        freq INTEGER,
        PRIMARY KEY (first, second, third, fourth)
    );

    CREATE TABLE Fgram (
        first   INTEGER,
        second INTEGER,
        third INTEGER,
        fourth INTEGER,
        fifth INTEGER,
        freq INTEGER,
        PRIMARY KEY (first, second, third, fourth,fifth)
    )

    ''')


# main programme
create_tables()
conn.close()
