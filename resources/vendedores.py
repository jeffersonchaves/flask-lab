from __main__ import app, connectionFactory
from flask import render_template
from models.seller import Seller


@app.route('/vendedores', methods=["GET"])
def list_all():
    sellers = []

    conn = connectionFactory.get_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seller")
    rows = cursor.fetchall()

    for row in rows:
        seller = Seller(row['Name'])
        sellers.append(seller)

    return render_template("index.html", sellers=sellers)


@app.route('/vendedores/<int:id>')
def find_by_id(id: int):
    conn = connectionFactory.get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM seller WHERE Id={id}")
    row = cursor.fetchone()

    if row:
        seller = Seller(row['Name'])
        return f"você selecionou o vendedor {seller}"

    return "vazio????"


@app.route('/vendedores/', methods=["POST"])
def method_name2():
    return "CADASTRAR"
