CREATE TABLE book (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author TEXT,
  editor TEXT,
  title TEXT,
  publisher TEXT,
  year INTEGER,
  volume TEXT,
  number INTEGER,
  pages TEXT,
  month INTEGER,
  note TEXT,
  doi TEXT,
  issn INTEGER,
  isbn INTEGER

);

CREATE TABLE article (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author TEXT,
  title TEXT,
  journal TEXT,
  year INTEGER,
  volume TEXT,
  number INTEGER,
  pages TEXT,
  month INTEGER,
  note TEXT,
  doi TEXT,
  issn INTEGER,
  zblnumber TEXT,
  eprint TEXT

);

CREATE TABLE inproceedings (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author TEXT,
  title TEXT,
  booktitle TEXT,
  year INTEGER,
  editor TEXT,
  volume TEXT,
  number INTEGER,
  series TEXT,
  pages TEXT,
  month INTEGER,
  address TEXT,
  organization TEXT,
  publisher TEXT,
  note TEXT,
  annote TEXT

);