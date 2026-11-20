from mysql.connector import Error

from connection_dao import close_connection, get_connection


def inserir_setor(nome, capacidade_maxima):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = "INSERT INTO Setor (nome, capacidade_maxima) VALUES (%s, %s)"

    try:
        cursor.execute(sql, (nome, capacidade_maxima))
        conn.commit()

        return cursor.lastrowid

    except Error as e:
        print(f"Erro ao inserir setor: {e}")
        conn.rollback()
        return None

    finally:
        close_connection(conn, cursor)


def listar_setores():
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, nome, capacidade_maxima FROM Setor ORDER BY id"

    try:
        cursor.execute(sql)
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao listar setores: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_setor_por_id(id_setor):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = "SELECT id, nome, capacidade_maxima FROM Setor WHERE id = %s"

    try:
        cursor.execute(sql, (id_setor,))
        return cursor.fetchone()

    except Error as e:
        print(f"Erro ao buscar setor: {e}")
        return None

    finally:
        close_connection(conn, cursor)


def buscar_setor_por_nome(nome):
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, nome, capacidade_maxima FROM Setor WHERE nome = %s"

    try:
        cursor.execute(sql, (nome,))
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao buscar setores: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_setor_por_capacidade(capacidade_maxima):
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, nome, capacidade_maxima FROM Setor WHERE capacidade_maxima = %s"

    try:
        cursor.execute(sql, (capacidade_maxima,))
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao buscar setores: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def atualizar_setor(id_setor, nome, capacidade_maxima):
    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    sql = "UPDATE Setor SET nome = %s, capacidade_maxima = %s WHERE id = %s"

    try:
        cursor.execute(sql, (nome, capacidade_maxima, id_setor))
        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao atualizar setor: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)


def remover_setor(id_setor):
    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    sql = "DELETE FROM Setor WHERE id = %s"

    try:
        cursor.execute(sql, (id_setor,))
        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao remover setor: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)