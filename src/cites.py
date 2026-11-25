
from config import db
from sqlalchemy import text


def add_book(book_data):
    sql = text("""
        INSERT INTO book (
            author,
            editor,
            title,
            publisher,
            year,
            volume,
            number,
            pages,
            month,
            note,
            doi,
            issn,
            isbn
        )
        VALUES (
            :author,
            :editor,
            :title,
            :publisher,
            :year,
            :volume,
            :number,
            :pages,
            :month,
            :note,
            :doi,
            :issn,
            :isbn
        )
    """)

    db.session.execute(sql, book_data)
    db.session.commit()


def add_article(article_data):
    sql = text("""
        INSERT INTO article (
            author,
            title,
            journal,
            year,
            volume,
            number,
            pages,
            month,
            note,
            doi,
            issn,
            zblnumber,
            eprint
        )
        VALUES (
            :author,
            :title,
            :journal,
            :year,
            :volume,
            :number,
            :pages,
            :month,
            :note,
            :doi,
            :issn,
            :zblnumber,
            :eprint
        )
    """)

    db.session.execute(sql, article_data)
    db.session.commit()


def add_inproceedings(inproceedings_data):
    sql = text("""
        INSERT INTO inproceedings (
            author,
            title,
            booktitle,
            year,
            editor,
            volume,
            number,
            series,
            pages,
            month,
            address,
            organization,
            publisher,
            note,
            annote
        )
        VALUES (
            :author,
            :title,
            :booktitle,
            :year,
            :editor,
            :volume,
            :number,
            :series,
            :pages,
            :month,
            :address,
            :organization,
            :publisher,
            :note,
            :annote
        )
    """)

    db.session.execute(sql, inproceedings_data)
    db.session.commit()


def get_references():
    references = []

    sql = text("SELECT * FROM book ORDER BY id")
    result = db.session.execute(sql)
    for reference in result:
        references.append(reference)

    sql = text("SELECT * FROM article ORDER BY id")
    result = db.session.execute(sql)
    for reference in result:
        references.append(reference)

    sql = text("SELECT * FROM inproceedings ORDER BY id")
    result = db.session.execute(sql)
    for reference in result:
        references.append(reference)

    return references
