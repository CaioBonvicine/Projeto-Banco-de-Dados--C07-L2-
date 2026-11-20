
from mysql.connector import Error

from connection_dao import close_connection, get_connection

def consultar_vagas_dispositivos():
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = """
        SELECT
            Vaga.codigo AS vaga,
            Dispositivo.id AS id_dispositivo
        FROM Vaga
        INNER JOIN `Dispositovo_Detecção` AS Dispositivo
            ON Vaga.Dispositovo_Detecção_id = Dispositivo.id
        ORDER BY Vaga.codigo
    """

    try:
        cursor.execute(sql)
        return cursor.fetchall()

    except Error as e:
        print(f"Erro na consulta de vagas e dispositivos: {e}")
        return []

    finally:
        close_connection(conn, cursor)

def consultar_clientes_veiculos():
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = """
        SELECT
            Cliente.nome AS cliente,
            Veiculo.placa AS placa,
            Veiculo.modelo AS modelo
        FROM Cliente
        INNER JOIN Veiculo
            ON Cliente.id = Veiculo.Cliente_id
        ORDER BY Cliente.nome
    """

    try:
        cursor.execute(sql)
        return cursor.fetchall()

    except Error as e:
        print(f"Erro na consulta de clientes e veículos: {e}")
        return []

    finally:
        close_connection(conn, cursor)

def consultar_veiculos_vagas():
    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    sql = """
        SELECT
            Veiculo.placa AS placa,
            Veiculo.modelo AS modelo,
            Vaga.codigo AS vaga,
            Registro_Estacionamento.data_hora_entrada,
            Registro_Estacionamento.data_hora_saida
        FROM Veiculo
        INNER JOIN Registro_Estacionamento
            ON Veiculo.id = Registro_Estacionamento.Veiculo_id
        INNER JOIN Vaga
            ON Registro_Estacionamento.Vaga_id = Vaga.id
        ORDER BY Veiculo.placa, Registro_Estacionamento.data_hora_entrada
    """

    try:
        cursor.execute(sql)
        return cursor.fetchall()

    except Error as e:
        print(f"Erro na consulta de veículos e vagas: {e}")
        return []

    finally:
        close_connection(conn, cursor)