from flask import Flask, render_template
from database.connection import ConnectionFactory

app = Flask(__name__)  # sao 2 underlines antes e 2 depois

connectionFactory = ConnectionFactory(app)


# import declared routes
import resources.vendedores


# 3 rodar nossa aplicacao
if __name__ == "__main__":
    app.run(debug=True)
