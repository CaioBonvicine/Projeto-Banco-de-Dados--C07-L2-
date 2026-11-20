import mysql.connector
from mysql.connector import Error

# Dados de acesso ao banco.
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "usuario_supervisor",
    "password": "Teste_Supervisor#2026",
    "database": "mydb",
}

def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            return connection

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")

    return None

def close_connection(connection, cursor=None):
    try:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()

    except Error as e:
        print(f"Erro ao fechar a conexão: {e}")

# Teste de conexão.
if __name__ == "__main__":

    conn = get_connection()

    if conn:
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT DATABASE()")

            banco = cursor.fetchone()[0]

            print("Conexão estabelecida com sucesso!")
            print(f"Banco selecionado: {banco}")

        except Error as e:
            print(f"Erro ao verificar o banco: {e}")

        finally:
            close_connection(conn, cursor)