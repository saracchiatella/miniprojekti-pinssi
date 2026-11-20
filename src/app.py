from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from config import app, test_env
import cites

@app.route("/")
def index():
    return render_template("index.html", title="home")

@app.route("/add_reference")
def add_reference():
    return render_template("add_reference.html", title="add_reference")

@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        # muodostetaan lomakkeen kentistä sanakirja:
        book_data = {
            "author": request.form.get("author"),
            "editor": request.form.get("editor"),
            "title": request.form.get("title"),
            "publisher": request.form.get("publisher"),
            "year": request.form.get("year"),
            "volume": request.form.get("volume"),
            "number": request.form.get("number"),
            "pages": request.form.get("pages"),
            "month": request.form.get("month"),
            "note": request.form.get("note"),
            "doi": request.form.get("doi"),
            "issn": request.form.get("issn"),
            "isbn": request.form.get("isbn"),
            }

        # lisätään kirja tietokantaan:
        cites.add_book(book_data)

        return redirect("/references")
    return render_template("book.html", title="book")

@app.route("/references")
def references():
    references = cites.get_references()
    return render_template("references.html", references=references, title="references")

#tämä reitti on testausta varten :)
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
