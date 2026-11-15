from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from config import app, test_env

@app.route("/")
def index():
    return render_template("index.html", title="home")

@app.route("/add_reference")
def add_reference():
    return render_template("add_reference.html", title="add_reference")

#tämä reitti on testausta varten :)
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
