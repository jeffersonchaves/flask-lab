from flask import Flask, render_template
from database.connection import ConnectionFactory
from outro import nome

app = Flask(__name__)  # sao 2 underlines antes e 2 depois

connectionFactory = ConnectionFactory(app)


# 1 rota -> meusite.com.br/ meusite.com.br/contatos
# 2 funcao


@app.route("/home/")
@app.route("/")
def index():
    conn = connectionFactory.getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seller")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # cursor = conn.cursor()
    # cursor.execute("SELECT * from seller")
    # data = cursor.fetchone()

    # print(data)

    return render_template("index.html", notic=rows)


@app.route("/contato/")
def contato():
    return "contatos"


@app.route('/vendedores', methods=["GET"])
def method_name():
    conn = connectionFactory.getConnection()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seller")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # cursor = conn.cursor()
    # cursor.execute("SELECT * from seller")
    # data = cursor.fetchone()

    # print(data)

    return render_template("index.html", notic=rows)


@app.route('/vendedores/<int:id>')
def vendedor(id: int):
    conn = connectionFactory.getConnection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM seller WHERE Id={id}")
    row = cursor.fetchone()

    return f"você selecionou o vendedor {row}"


@app.route('/vendedores/', methods=["POST"])
def method_name2():
    return "CADASTRAR"


# 3 rodar nossa aplicacao
if __name__ == "__main__":
    app.run(debug=True)
