from mysql.connector import Error

from connection_dao import close_connection, get_connection


def inserir_cliente(nome, cpf, telefone=None):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = """
        INSERT INTO Cliente (nome, cpf, telefone)
        VALUES (%s, %s, %s)
    """

    try:
        cursor.execute(sql, (nome, cpf, telefone))
        conn.commit()

        return cursor.lastrowid

    except Error as e:
        print(f"Erro ao inserir cliente: {e}")
        conn.rollback()
        return None

    finally:
        close_connection(conn, cursor)


def listar_clientes():
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, nome, cpf, telefone FROM Cliente ORDER BY id"

    try:
        cursor.execute(sql)
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao listar clientes: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_cliente_por_id(id_cliente):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = "SELECT id, nome, cpf, telefone FROM Cliente WHERE id = %s"

    try:
        cursor.execute(sql, (id_cliente,))
        return cursor.fetchone()

    except Error as e:
        print(f"Erro ao buscar cliente: {e}")
        return None

    finally:
        close_connection(conn, cursor)


def buscar_cliente_por_nome(nome):
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, nome, cpf, telefone FROM Cliente WHERE nome = %s"

    try:
        cursor.execute(sql, (nome,))
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao buscar cliente: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_cliente_por_cpf(cpf):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = "SELECT id, nome, cpf, telefone FROM Cliente WHERE cpf = %s"

    try:
        cursor.execute(sql, (cpf,))
        return cursor.fetchone()

    except Error as e:
        print(f"Erro ao buscar cliente: {e}")
        return None

    finally:
        close_connection(conn, cursor)


def atualizar_cliente(id_cliente, nome, cpf, telefone):
    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    sql = """
        UPDATE Cliente
        SET nome = %s, cpf = %s, telefone = %s
        WHERE id = %s
    """

    try:
        cursor.execute(sql, (nome, cpf, telefone, id_cliente))
        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao atualizar cliente: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)


def remover_cliente(id_cliente):
    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    sql = "DELETE FROM Cliente WHERE id = %s"

    try:
        cursor.execute(sql, (id_cliente,))
        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao remover cliente: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)