from mysql.connector import Error

from connection_dao import close_connection, get_connection


def inserir_vaga(codigo, ocupacao, setor_id, dispositivo_id):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = """
        INSERT INTO Vaga (codigo, `ocupação`, Setor_id, Dispositovo_Detecção_id)
        VALUES (%s, %s, %s, %s)
    """

    try:
        cursor.execute(sql, (codigo, ocupacao, setor_id, dispositivo_id))
        conn.commit()

        return cursor.lastrowid

    except Error as e:
        print(f"Erro ao inserir vaga: {e}")
        conn.rollback()
        return None

    finally:
        close_connection(conn, cursor)


def listar_vagas():
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, codigo, `ocupação`, Setor_id, Dispositovo_Detecção_id FROM Vaga ORDER BY id"

    try:
        cursor.execute(sql)
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao listar vagas: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_vaga_por_id(id_vaga):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = "SELECT id, codigo, `ocupação`, Setor_id, Dispositovo_Detecção_id FROM Vaga WHERE id = %s"

    try:
        cursor.execute(sql, (id_vaga,))
        return cursor.fetchone()

    except Error as e:
        print(f"Erro ao buscar vaga: {e}")
        return None

    finally:
        close_connection(conn, cursor)


def buscar_vaga_por_codigo(codigo):
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, codigo, `ocupação`, Setor_id, Dispositovo_Detecção_id FROM Vaga WHERE codigo = %s"

    try:
        cursor.execute(sql, (codigo,))
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao buscar vagas: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_vagas_por_ocupacao(ocupacao):
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, codigo, `ocupação`, Setor_id, Dispositovo_Detecção_id FROM Vaga WHERE `ocupação` = %s"

    try:
        cursor.execute(sql, (ocupacao,))
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao buscar vagas: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_vagas_por_setor(setor_id):
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, codigo, `ocupação`, Setor_id, Dispositovo_Detecção_id FROM Vaga WHERE Setor_id = %s"

    try:
        cursor.execute(sql, (setor_id,))
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao buscar vagas: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_vaga_por_dispositivo(dispositivo_id):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = "SELECT id, codigo, `ocupação`, Setor_id, Dispositovo_Detecção_id FROM Vaga WHERE Dispositovo_Detecção_id = %s"

    try:
        cursor.execute(sql, (dispositivo_id,))
        return cursor.fetchone()

    except Error as e:
        print(f"Erro ao buscar vaga: {e}")
        return None

    finally:
        close_connection(conn, cursor)


def atualizar_vaga(id_vaga, codigo, ocupacao, setor_id, dispositivo_id):
    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    sql = """
        UPDATE Vaga
        SET codigo = %s, `ocupação` = %s, Setor_id = %s,
            Dispositovo_Detecção_id = %s
        WHERE id = %s
    """

    try:
        cursor.execute(sql, (codigo, ocupacao, setor_id, dispositivo_id, id_vaga))
        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao atualizar vaga: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)


def remover_vaga(id_vaga):
    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    sql = "DELETE FROM Vaga WHERE id = %s"

    try:
        cursor.execute(sql, (id_vaga,))
        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao remover vaga: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)