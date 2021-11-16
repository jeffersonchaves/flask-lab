from flaskext.mysql import MySQL, pymysql
from pymysql import Connection


class ConnectionFactory:

    app = None
    mysqlConnection = None

    def __init__(self, app):

        self.app = app
        self.app.config['MYSQL_DATABASE_USER'] = 'jrh723dnnjs1u5ce'
        self.app.config['MYSQL_DATABASE_PASSWORD'] = 'w8hzubq4xseu9djj'
        self.app.config['MYSQL_DATABASE_DB'] = 'gcj94fo1u2n7n1ze'
        self.app.config['MYSQL_DATABASE_HOST'] = 'z5zm8hebixwywy9d.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'

        mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)
        mysql.init_app(self.app)
        self.mysqlConnection = mysql.connect()

    def get_connection(self) -> Connection:
        return self.mysqlConnection
