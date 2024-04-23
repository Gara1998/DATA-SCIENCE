import json
from flask import Flask, request, jsonify
import sqlite3
import os

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to my API conected to my books database"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def get_all():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    select_books = "SELECT * FROM books"
    result = cursor.execute(select_books).fetchall()
    connection.close()
    return jsonify(result)

# 1.Ruta para obtener el conteo de libros por autor ordenados de forma descendente
@app.route('/api/v1/resources/booksbyauthor/', methods=['GET'])
def author_books():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    select_books = '''
    SELECT 
        author,
        COUNT(*) 
    FROM books 
    GROUP BY 1 
    ORDER BY 2 DESC'''
    result = cursor.execute(select_books).fetchall()
    connection.close()
    return jsonify(result)

# 2.Ruta para obtener los libros de un autor como argumento en la llamada
@app.route('/api/v1/resources/books/author', methods=['GET'])
def book_author():
    if 'author' in request.args:
        author = "%"+request.args['author']+"%"
        connection = sqlite3.connect('books.db')
        cursor = connection.cursor()
        select_books = '''
        SELECT 
            * 
        FROM books 
        WHERE author LIKE ?'''
        result = cursor.execute(select_books, (author,)).fetchall()
        connection.close()
        return jsonify(result)
    else:
        return "Author argument missing"


# 3.Ruta para obtener los libros filtrados por título, publicación y autor
@app.route('/api/v1/resources/books/filters', methods=['GET'])
def filters():    
    query = "SELECT * FROM books WHERE"
    filters = []
    if 'title' not in request.args and 'published' not in request.args and 'author' not in request.args:
        return "Filters missing"
    else:
        if 'title' in request.args:
            title = '%' + request.args['title'] + '%'
            query += " title LIKE ? AND"
            filters.append(title)
        if 'published' in request.args:
            published = request.args['published']
            query += " published = ? AND"
            filters.append(published)
        if 'author' in request.args:
            author = '%' + request.args['author'] + '%'
            query += " author LIKE ? AND"
            filters.append(author)
        connection = sqlite3.connect('books.db')
        cursor = connection.cursor()
        result = cursor.execute(query[:-4], filters).fetchall()
        return jsonify(result)

app.run()