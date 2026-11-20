from mysql.connector import Error

from connection_dao import close_connection, get_connection


def inserir_veiculo(placa, modelo, cliente_id):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = """
        INSERT INTO Veiculo (placa, modelo, Cliente_id)
        VALUES (%s, %s, %s)
    """

    try:
        cursor.execute(sql, (placa, modelo, cliente_id))
        conn.commit()

        return cursor.lastrowid

    except Error as e:
        print(f"Erro ao inserir veículo: {e}")
        conn.rollback()
        return None

    finally:
        close_connection(conn, cursor)


def listar_veiculos():
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, placa, modelo, Cliente_id FROM Veiculo ORDER BY id"

    try:
        cursor.execute(sql)
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao listar veículos: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_veiculo_por_id(id_veiculo):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = "SELECT id, placa, modelo, Cliente_id FROM Veiculo WHERE id = %s"

    try:
        cursor.execute(sql, (id_veiculo,))
        return cursor.fetchone()

    except Error as e:
        print(f"Erro ao buscar veículo: {e}")
        return None

    finally:
        close_connection(conn, cursor)


def buscar_veiculo_por_placa(placa):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = "SELECT id, placa, modelo, Cliente_id FROM Veiculo WHERE placa = %s"

    try:
        cursor.execute(sql, (placa,))
        return cursor.fetchone()

    except Error as e:
        print(f"Erro ao buscar veículo: {e}")
        return None

    finally:
        close_connection(conn, cursor)


def buscar_veiculo_por_modelo(modelo):
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, placa, modelo, Cliente_id FROM Veiculo WHERE modelo = %s"

    try:
        cursor.execute(sql, (modelo,))
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao buscar veículos: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_veiculos_por_cliente(cliente_id):
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, placa, modelo, Cliente_id FROM Veiculo WHERE Cliente_id = %s"

    try:
        cursor.execute(sql, (cliente_id,))
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao buscar veículos: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def atualizar_veiculo(id_veiculo, placa, modelo, cliente_id):
    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    sql = """
        UPDATE Veiculo
        SET placa = %s, modelo = %s, Cliente_id = %s
        WHERE id = %s
    """

    try:
        cursor.execute(sql, (placa, modelo, cliente_id, id_veiculo))
        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao atualizar veículo: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)


def remover_veiculo(id_veiculo):
    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    sql = "DELETE FROM Veiculo WHERE id = %s"

    try:
        cursor.execute(sql, (id_veiculo,))
        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao remover veículo: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)