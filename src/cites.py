
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


def get_references():
    sql = text("SELECT * FROM book ORDER BY id")

    result = db.session.execute(sql)

    references = result.fetchall()

    return references
