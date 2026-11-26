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
            "edition": request.form.get("edition"),
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

@app.route("/article", methods=["GET", "POST"])
def article():
    if request.method == "POST":
        article_data = {
            "author": request.form.get("author"),
            "title": request.form.get("title"),
            "journal": request.form.get("journal"),
            "year": request.form.get("year"),
            "volume": request.form.get("volume"),
            "number": request.form.get("number"),
            "pages": request.form.get("pages"),
            "month": request.form.get("month"),
            "note": request.form.get("note"),
            "doi": request.form.get("doi"),
            "issn": request.form.get("issn"),
            "zblnumber": request.form.get("zblnumber"),
            "eprint": request.form.get("eprint"),
        }

        cites.add_article(article_data)

        return redirect("/references")
    return render_template("article.html", title="article")

@app.route("/inproceedings", methods=["GET", "POST"])
def inproceedings():
    if request.method == "POST":
        inproceedings_data = {
            "author": request.form.get("author"),
            "title": request.form.get("title"),
            "booktitle": request.form.get("booktitle"),
            "year": request.form.get("year"),
            "editor": request.form.get("editor"),
            "volume": request.form.get("volume"),
            "number": request.form.get("number"),
            "series": request.form.get("series"),
            "pages": request.form.get("pages"),
            "month": request.form.get("month"),
            "address": request.form.get("address"),
            "organization": request.form.get("organization"),
            "publisher": request.form.get("publisher"),
            "note": request.form.get("note"),
            "annote": request.form.get("annote"),
        }

        cites.add_inproceedings(inproceedings_data)

        return redirect("/references")
    return render_template("inproceedings.html", title="inproceedings")


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
