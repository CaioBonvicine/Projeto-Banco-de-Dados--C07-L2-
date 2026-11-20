from mysql.connector import Error

from connection_dao import close_connection, get_connection


def inserir_dispositivo(endereco_mac):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = "INSERT INTO `Dispositovo_Detecção` (`endereço_mac`) VALUES (%s)"

    try:
        cursor.execute(sql, (endereco_mac,))
        conn.commit()

        return cursor.lastrowid

    except Error as e:
        print(f"Erro ao inserir dispositivo: {e}")
        conn.rollback()
        return None

    finally:
        close_connection(conn, cursor)


def listar_dispositivos():
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = "SELECT id, `endereço_mac` FROM `Dispositovo_Detecção` ORDER BY id"

    try:
        cursor.execute(sql)
        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao listar dispositivos: {e}")
        return []

    finally:
        close_connection(conn, cursor)


def buscar_dispositivo_por_id(id_dispositivo):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = "SELECT id, `endereço_mac` FROM `Dispositovo_Detecção` WHERE id = %s"

    try:
        cursor.execute(sql, (id_dispositivo,))
        return cursor.fetchone()

    except Error as e:
        print(f"Erro ao buscar dispositivo: {e}")
        return None

    finally:
        close_connection(conn, cursor)


def buscar_dispositivo_por_mac(endereco_mac):
    conn = get_connection()

    if conn is None:
        return None

    cursor = conn.cursor()

    sql = "SELECT id, `endereço_mac` FROM `Dispositovo_Detecção` WHERE `endereço_mac` = %s"

    try:
        cursor.execute(sql, (endereco_mac,))
        return cursor.fetchone()

    except Error as e:
        print(f"Erro ao buscar dispositivo: {e}")
        return None

    finally:
        close_connection(conn, cursor)


def atualizar_dispositivo(id_dispositivo, endereco_mac):
    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    sql = "UPDATE `Dispositovo_Detecção` SET `endereço_mac` = %s WHERE id = %s"

    try:
        cursor.execute(sql, (endereco_mac, id_dispositivo))
        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao atualizar dispositivo: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)


def remover_dispositivo(id_dispositivo):
    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    sql = "DELETE FROM `Dispositovo_Detecção` WHERE id = %s"

    try:
        cursor.execute(sql, (id_dispositivo,))
        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao remover dispositivo: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)