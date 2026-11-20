from mysql.connector import Error

from connection_dao import close_connection, get_connection


def inserir_registro(data_hora_entrada, data_hora_saida, veiculo_id, vaga_id):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = """
        INSERT INTO Registro_Estacionamento
        (data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id)
        VALUES (%s, %s, %s, %s)
    """

    try:
        cursor.execute(sql, (data_hora_entrada, data_hora_saida, veiculo_id, vaga_id))
        conn.commit()

        return cursor.lastrowid

    except Error as e:
        print(f"Erro ao inserir registro: {e}")
        conn.rollback()
        return None

    finally:
        close_connection(conn, cursor)


def listar_registros():
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id FROM Registro_Estacionamento ORDER BY id"

    try:
        cursor.execute(sql)
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao listar registros: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_registro_por_id(id_registro):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = "SELECT id, data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id FROM Registro_Estacionamento WHERE id = %s"

    try:
        cursor.execute(sql, (id_registro,))
        return cursor.fetchone()

    except Error as e:
        print(f"Erro ao buscar registro: {e}")
        return None

    finally:
        close_connection(conn, cursor)


def buscar_registros_por_veiculo(veiculo_id):
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id FROM Registro_Estacionamento WHERE Veiculo_id = %s"

    try:
        cursor.execute(sql, (veiculo_id,))
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao buscar registros: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_registros_por_vaga(vaga_id):
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id FROM Registro_Estacionamento WHERE Vaga_id = %s"

    try:
        cursor.execute(sql, (vaga_id,))
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao buscar registros: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_registros_por_data_entrada(data_hora_entrada):
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id FROM Registro_Estacionamento WHERE data_hora_entrada = %s"

    try:
        cursor.execute(sql, (data_hora_entrada,))
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao buscar registros: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_registros_em_aberto():
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id FROM Registro_Estacionamento WHERE data_hora_saida IS NULL"

    try:
        cursor.execute(sql)
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao buscar registros: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def atualizar_registro(id_registro, data_hora_entrada, data_hora_saida, veiculo_id, vaga_id):
    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    sql = """
        UPDATE Registro_Estacionamento
        SET data_hora_entrada = %s, data_hora_saida = %s,
            Veiculo_id = %s, Vaga_id = %s
        WHERE id = %s
    """

    try:
        cursor.execute(sql, (data_hora_entrada, data_hora_saida, veiculo_id, vaga_id, id_registro))
        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao atualizar registro: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)


def remover_registro(id_registro):
    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    try:
        sql = "SELECT Vaga_id, data_hora_saida FROM Registro_Estacionamento WHERE id = %s"
        cursor.execute(sql, (id_registro,))

        registro = cursor.fetchone()

        if registro is None:
            return False

        if registro[1] is None:
            sql = "UPDATE Vaga SET `ocupação` = 0 WHERE id = %s"
            cursor.execute(sql, (registro[0],))

        sql = "DELETE FROM Registro_Estacionamento WHERE id = %s"
        cursor.execute(sql, (id_registro,))

        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao remover registro: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)