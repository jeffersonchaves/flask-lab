from flask import Flask, render_template
from flaskext.mysql import MySQL, pymysql
from outro import nome

app = Flask(__name__)  # sao 2 underlines antes e 2 depois


app.config['MYSQL_DATABASE_USER'] = 'jrh723dnnjs1u5ce'
app.config['MYSQL_DATABASE_PASSWORD'] = 'w8hzubq4xseu9djj'
app.config['MYSQL_DATABASE_DB'] = 'gcj94fo1u2n7n1ze'
app.config['MYSQL_DATABASE_HOST'] = 'z5zm8hebixwywy9d.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)
mysql.init_app(app)

conn = mysql.connect()

# 1 rota -> meusite.com.br/ meusite.com.br/contatos
# 2 funcao


@app.route("/home/")
@app.route("/")
def index():
    conn = mysql.connect()
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
    c = conn.cursor()
    c.execute("SELECT * FROM seller")
    rows = c.fetchall()
    for row in rows:
        print(row)

    # cursor = conn.cursor()
    # cursor.execute("SELECT * from seller")
    # data = cursor.fetchone()

    # print(data)

    return render_template("index.html", notic=rows)


@app.route('/vendedores/<int:id>')
def vendedor(id: int):

    c = conn.cursor()
    c.execute(f"SELECT * FROM seller WHERE Id={id}")
    row = c.fetchone()

    return f"você selecionou o vendedor {row}"


@app.route('/vendedores/', methods=["POST"])
def method_name2():
    return "CADASTRAR"


# 3 rodar nossa aplicacao
if __name__ == "__main__":
    app.run(debug=True)
