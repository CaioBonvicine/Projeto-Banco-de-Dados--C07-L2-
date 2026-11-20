from cliente_dao import (
    inserir_cliente,
    listar_clientes,
    buscar_cliente_por_id,
    buscar_cliente_por_nome,
    buscar_cliente_por_cpf,
    atualizar_cliente,
    remover_cliente
)

from veiculo_dao import (
    inserir_veiculo,
    listar_veiculos,
    buscar_veiculo_por_id,
    buscar_veiculo_por_placa,
    buscar_veiculo_por_modelo,
    buscar_veiculos_por_cliente,
    atualizar_veiculo,
    remover_veiculo
)

from setor_dao import (
    inserir_setor,
    listar_setores,
    buscar_setor_por_id,
    buscar_setor_por_nome,
    buscar_setor_por_capacidade,
    atualizar_setor,
    remover_setor
)

from dispositivo_dao import (
    inserir_dispositivo,
    listar_dispositivos,
    buscar_dispositivo_por_id,
    buscar_dispositivo_por_mac,
    atualizar_dispositivo,
    remover_dispositivo
)

from vaga_dao import (
    inserir_vaga,
    listar_vagas,
    buscar_vaga_por_id,
    buscar_vaga_por_codigo,
    buscar_vagas_por_ocupacao,
    buscar_vagas_por_setor,
    buscar_vaga_por_dispositivo,
    atualizar_vaga,
    remover_vaga
)

from registro_estacionamento_dao import (
    inserir_registro,
    listar_registros,
    buscar_registro_por_id,
    buscar_registros_por_veiculo,
    buscar_registros_por_vaga,
    buscar_registros_por_data_entrada,
    buscar_registros_em_aberto,
    atualizar_registro,
    remover_registro
)

from consultas_dao import (
    consultar_vagas_dispositivos,
    consultar_clientes_veiculos,
    consultar_veiculos_vagas
)


def ler_texto(pergunta):
    return input(pergunta).strip()


def ler_inteiro(pergunta):
    while True:
        try:
            return int(input(pergunta))
        except ValueError:
            print("Digite um número inteiro.")


def ler_ocupacao():
    while True:
        ocupacao = ler_inteiro("Ocupação (0 = Livre / 1 = Ocupada): ")

        if ocupacao in (0, 1):
            return ocupacao

        print("Digite 0 para livre ou 1 para ocupada.")


def mostrar(registros):
    if not registros:
        print("Nenhum registro encontrado.")
        return

    for registro in registros:
        print(registro)


def mostrar_unico(registro):
    if registro is None:
        mostrar([])
    else:
        mostrar([registro])


def pausar():
    input("\nPressione Enter para continuar...")


def confirmar_remocao(funcao, entidade):
    id_registro = ler_inteiro(f"ID do {entidade}: ")

    confirmacao = ler_texto(
        f"Confirma a remoção do {entidade} {id_registro}? (s/n): "
    ).lower()

    if confirmacao == "s":
        if funcao(id_registro):
            print("Registro removido com sucesso.")
        else:
            print("Não foi possível remover o registro.")
    else:
        print("Remoção cancelada.")


def executar_menu(menu, acoes):
    while True:
        print(menu)
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "0":
            break

        acao = acoes.get(escolha)

        if acao is None:
            print("Opção inválida.")
        else:
            acao()

            if acao not in MENUS:
                pausar()


MENU_PRINCIPAL = """
========= SISTEMA INTELIGENTE DE ESTACIONAMENTO =========

1 - Gerenciar Clientes
2 - Gerenciar Veículos
3 - Gerenciar Setores
4 - Gerenciar Dispositivos
5 - Gerenciar Vagas
6 - Gerenciar Registros de Estacionamento
7 - Consultas JOIN

0 - Sair

"""

MENU_CLIENTES = """
=============== GERENCIAR CLIENTES ===============

1 - Cadastrar cliente
2 - Listar todos os clientes
3 - Buscar cliente por filtro
4 - Atualizar cliente
5 - Remover cliente

0 - Voltar

"""

MENU_BUSCA_CLIENTES = """
=============== BUSCAR CLIENTE ===============

1 - Buscar por ID
2 - Buscar por nome
3 - Buscar por CPF

0 - Voltar

"""

MENU_VEICULOS = """
=============== GERENCIAR VEÍCULOS ===============

1 - Cadastrar veículo
2 - Listar todos os veículos
3 - Buscar veículo por filtro
4 - Atualizar veículo
5 - Remover veículo

0 - Voltar

"""

MENU_BUSCA_VEICULOS = """
=============== BUSCAR VEÍCULO ===============

1 - Buscar por ID
2 - Buscar por placa
3 - Buscar por modelo
4 - Buscar por cliente

0 - Voltar

"""

MENU_SETORES = """
=============== GERENCIAR SETORES ===============

1 - Cadastrar setor
2 - Listar todos os setores
3 - Buscar setor por filtro
4 - Atualizar setor
5 - Remover setor

0 - Voltar

"""

MENU_BUSCA_SETORES = """
=============== BUSCAR SETOR ===============

1 - Buscar por ID
2 - Buscar por nome
3 - Buscar por capacidade máxima

0 - Voltar

"""

MENU_DISPOSITIVOS = """
=============== GERENCIAR DISPOSITIVOS ===============

1 - Cadastrar dispositivo
2 - Listar todos os dispositivos
3 - Buscar dispositivo por filtro
4 - Atualizar dispositivo
5 - Remover dispositivo

0 - Voltar

"""

MENU_BUSCA_DISPOSITIVOS = """
=============== BUSCAR DISPOSITIVO ===============

1 - Buscar por ID
2 - Buscar por endereço MAC

0 - Voltar

"""

MENU_VAGAS = """
=============== GERENCIAR VAGAS ===============

1 - Cadastrar vaga
2 - Listar todas as vagas
3 - Buscar vaga por filtro
4 - Atualizar vaga
5 - Remover vaga

0 - Voltar

"""

MENU_BUSCA_VAGAS = """
=============== BUSCAR VAGA ===============

1 - Buscar por ID
2 - Buscar por código
3 - Buscar por ocupação
4 - Buscar por setor
5 - Buscar por dispositivo

0 - Voltar

"""

MENU_REGISTROS = """
========= GERENCIAR REGISTROS DE ESTACIONAMENTO =========

1 - Registrar estacionamento
2 - Listar todos os registros
3 - Buscar registro por filtro
4 - Atualizar registro
5 - Remover registro

0 - Voltar

"""

MENU_BUSCA_REGISTROS = """
=============== BUSCAR REGISTRO ===============

1 - Buscar por ID
2 - Buscar por veículo
3 - Buscar por vaga
4 - Buscar por data e hora de entrada
5 - Listar registros em aberto

0 - Voltar

"""

MENU_CONSULTAS = """
================ CONSULTAS JOIN ================

1 - Vagas e dispositivos (1:1)
2 - Clientes e veículos (1:N)
3 - Veículos e vagas (N:M)

0 - Voltar

"""


def opcao_inserir_cliente():
    nome = ler_texto("Nome: ")
    cpf = ler_texto("CPF: ")
    telefone = ler_texto("Telefone (Enter para deixar vazio): ")

    if telefone == "":
        telefone = None

    novo_id = inserir_cliente(nome, cpf, telefone)

    if novo_id is not None:
        print(f"Cliente cadastrado com sucesso. ID: {novo_id}")
    else:
        print("Não foi possível cadastrar o cliente.")


def opcao_listar_clientes():
    print("\nClientes cadastrados:")
    mostrar(listar_clientes())


def opcao_buscar_cliente_id():
    id_cliente = ler_inteiro("ID do cliente: ")
    mostrar_unico(buscar_cliente_por_id(id_cliente))


def opcao_buscar_cliente_nome():
    nome = ler_texto("Nome do cliente: ")
    mostrar(buscar_cliente_por_nome(nome))


def opcao_buscar_cliente_cpf():
    cpf = ler_texto("CPF do cliente: ")
    mostrar_unico(buscar_cliente_por_cpf(cpf))


def opcao_atualizar_cliente():
    id_cliente = ler_inteiro("ID do cliente: ")
    nome = ler_texto("Novo nome: ")
    cpf = ler_texto("Novo CPF: ")
    telefone = ler_texto("Novo telefone (Enter para deixar vazio): ")

    if telefone == "":
        telefone = None

    if atualizar_cliente(id_cliente, nome, cpf, telefone):
        print("Cliente atualizado com sucesso.")
    else:
        print("Nenhum registro foi alterado. Confira o ID e os valores informados.")


def opcao_remover_cliente():
    confirmar_remocao(remover_cliente, "cliente")


def menu_busca_clientes():
    executar_menu(MENU_BUSCA_CLIENTES, ACOES_BUSCA_CLIENTES)


def menu_clientes():
    executar_menu(MENU_CLIENTES, ACOES_CLIENTES)


def opcao_inserir_veiculo():
    placa = ler_texto("Placa: ")
    modelo = ler_texto("Modelo (Enter para deixar vazio): ")
    cliente_id = ler_inteiro("ID do cliente: ")

    if modelo == "":
        modelo = None

    novo_id = inserir_veiculo(placa, modelo, cliente_id)

    if novo_id is not None:
        print(f"Veículo cadastrado com sucesso. ID: {novo_id}")
    else:
        print("Não foi possível cadastrar o veículo.")


def opcao_listar_veiculos():
    print("\nVeículos cadastrados:")
    mostrar(listar_veiculos())


def opcao_buscar_veiculo_id():
    id_veiculo = ler_inteiro("ID do veículo: ")
    mostrar_unico(buscar_veiculo_por_id(id_veiculo))


def opcao_buscar_veiculo_placa():
    placa = ler_texto("Placa do veículo: ")
    mostrar_unico(buscar_veiculo_por_placa(placa))


def opcao_buscar_veiculo_modelo():
    modelo = ler_texto("Modelo do veículo: ")
    mostrar(buscar_veiculo_por_modelo(modelo))


def opcao_buscar_veiculo_cliente():
    cliente_id = ler_inteiro("ID do cliente: ")
    mostrar(buscar_veiculos_por_cliente(cliente_id))


def opcao_atualizar_veiculo():
    id_veiculo = ler_inteiro("ID do veículo: ")
    placa = ler_texto("Nova placa: ")
    modelo = ler_texto("Novo modelo (Enter para deixar vazio): ")
    cliente_id = ler_inteiro("Novo ID do cliente: ")

    if modelo == "":
        modelo = None

    if atualizar_veiculo(id_veiculo, placa, modelo, cliente_id):
        print("Veículo atualizado com sucesso.")
    else:
        print("Nenhum registro foi alterado. Confira o ID e os valores informados.")


def opcao_remover_veiculo():
    confirmar_remocao(remover_veiculo, "veículo")


def menu_busca_veiculos():
    executar_menu(MENU_BUSCA_VEICULOS, ACOES_BUSCA_VEICULOS)


def menu_veiculos():
    executar_menu(MENU_VEICULOS, ACOES_VEICULOS)


def opcao_inserir_setor():
    nome = ler_texto("Nome do setor: ")
    capacidade_maxima = ler_inteiro("Capacidade máxima: ")

    novo_id = inserir_setor(nome, capacidade_maxima)

    if novo_id is not None:
        print(f"Setor cadastrado com sucesso. ID: {novo_id}")
    else:
        print("Não foi possível cadastrar o setor.")


def opcao_listar_setores():
    print("\nSetores cadastrados:")
    mostrar(listar_setores())


def opcao_buscar_setor_id():
    id_setor = ler_inteiro("ID do setor: ")
    mostrar_unico(buscar_setor_por_id(id_setor))


def opcao_buscar_setor_nome():
    nome = ler_texto("Nome do setor: ")
    mostrar(buscar_setor_por_nome(nome))


def opcao_buscar_setor_capacidade():
    capacidade = ler_inteiro("Capacidade máxima: ")
    mostrar(buscar_setor_por_capacidade(capacidade))


def opcao_atualizar_setor():
    id_setor = ler_inteiro("ID do setor: ")
    nome = ler_texto("Novo nome: ")
    capacidade_maxima = ler_inteiro("Nova capacidade máxima: ")

    if atualizar_setor(id_setor, nome, capacidade_maxima):
        print("Setor atualizado com sucesso.")
    else:
        print("Nenhum registro foi alterado. Confira o ID e os valores informados.")


def opcao_remover_setor():
    confirmar_remocao(remover_setor, "setor")


def menu_busca_setores():
    executar_menu(MENU_BUSCA_SETORES, ACOES_BUSCA_SETORES)


def menu_setores():
    executar_menu(MENU_SETORES, ACOES_SETORES)


def opcao_inserir_dispositivo():
    endereco_mac = ler_texto("Endereço MAC: ")
    novo_id = inserir_dispositivo(endereco_mac)

    if novo_id is not None:
        print(f"Dispositivo cadastrado com sucesso. ID: {novo_id}")
    else:
        print("Não foi possível cadastrar o dispositivo.")


def opcao_listar_dispositivos():
    print("\nDispositivos cadastrados:")
    mostrar(listar_dispositivos())


def opcao_buscar_dispositivo_id():
    id_dispositivo = ler_inteiro("ID do dispositivo: ")
    mostrar_unico(buscar_dispositivo_por_id(id_dispositivo))


def opcao_buscar_dispositivo_mac():
    endereco_mac = ler_texto("Endereço MAC: ")
    mostrar_unico(buscar_dispositivo_por_mac(endereco_mac))


def opcao_atualizar_dispositivo():
    id_dispositivo = ler_inteiro("ID do dispositivo: ")
    endereco_mac = ler_texto("Novo endereço MAC: ")

    if atualizar_dispositivo(id_dispositivo, endereco_mac):
        print("Dispositivo atualizado com sucesso.")
    else:
        print("Nenhum registro foi alterado. Confira o ID e os valores informados.")


def opcao_remover_dispositivo():
    confirmar_remocao(remover_dispositivo, "dispositivo")


def menu_busca_dispositivos():
    executar_menu(MENU_BUSCA_DISPOSITIVOS, ACOES_BUSCA_DISPOSITIVOS)


def menu_dispositivos():
    executar_menu(MENU_DISPOSITIVOS, ACOES_DISPOSITIVOS)


def opcao_inserir_vaga():
    codigo = ler_texto("Código da vaga: ")
    ocupacao = ler_ocupacao()
    setor_id = ler_inteiro("ID do setor: ")
    dispositivo_id = ler_inteiro("ID do dispositivo: ")

    novo_id = inserir_vaga(codigo, ocupacao, setor_id, dispositivo_id)

    if novo_id is not None:
        print(f"Vaga cadastrada com sucesso. ID: {novo_id}")
    else:
        print("Não foi possível cadastrar a vaga.")


def opcao_listar_vagas():
    print("\nVagas cadastradas:")
    mostrar(listar_vagas())


def opcao_buscar_vaga_id():
    id_vaga = ler_inteiro("ID da vaga: ")
    mostrar_unico(buscar_vaga_por_id(id_vaga))


def opcao_buscar_vaga_codigo():
    codigo = ler_texto("Código da vaga: ")
    mostrar(buscar_vaga_por_codigo(codigo))


def opcao_buscar_vaga_ocupacao():
    ocupacao = ler_ocupacao()
    mostrar(buscar_vagas_por_ocupacao(ocupacao))


def opcao_buscar_vaga_setor():
    setor_id = ler_inteiro("ID do setor: ")
    mostrar(buscar_vagas_por_setor(setor_id))


def opcao_buscar_vaga_dispositivo():
    dispositivo_id = ler_inteiro("ID do dispositivo: ")
    mostrar_unico(buscar_vaga_por_dispositivo(dispositivo_id))


def opcao_atualizar_vaga():
    id_vaga = ler_inteiro("ID da vaga: ")
    codigo = ler_texto("Novo código: ")
    ocupacao = ler_ocupacao()
    setor_id = ler_inteiro("Novo ID do setor: ")
    dispositivo_id = ler_inteiro("Novo ID do dispositivo: ")

    if atualizar_vaga(id_vaga, codigo, ocupacao, setor_id, dispositivo_id):
        print("Vaga atualizada com sucesso.")
    else:
        print("Nenhum registro foi alterado. Confira o ID e os valores informados.")


def opcao_remover_vaga():
    confirmar_remocao(remover_vaga, "vaga")


def menu_busca_vagas():
    executar_menu(MENU_BUSCA_VAGAS, ACOES_BUSCA_VAGAS)


def menu_vagas():
    executar_menu(MENU_VAGAS, ACOES_VAGAS)


def opcao_inserir_registro():
    data_hora_entrada = ler_texto("Data e hora de entrada (AAAA-MM-DD HH:MM:SS): ")
    data_hora_saida = ler_texto("Data e hora de saída (Enter se ainda estiver estacionado): ")
    veiculo_id = ler_inteiro("ID do veículo: ")
    vaga_id = ler_inteiro("ID da vaga: ")

    if data_hora_saida == "":
        data_hora_saida = None

    novo_id = inserir_registro(data_hora_entrada, data_hora_saida, veiculo_id, vaga_id)

    if novo_id is not None:
        print(f"Registro cadastrado com sucesso. ID: {novo_id}")
    else:
        print("Não foi possível cadastrar o registro.")


def opcao_listar_registros():
    print("\nRegistros de estacionamento:")
    mostrar(listar_registros())


def opcao_buscar_registro_id():
    id_registro = ler_inteiro("ID do registro: ")
    mostrar_unico(buscar_registro_por_id(id_registro))


def opcao_buscar_registro_veiculo():
    veiculo_id = ler_inteiro("ID do veículo: ")
    mostrar(buscar_registros_por_veiculo(veiculo_id))


def opcao_buscar_registro_vaga():
    vaga_id = ler_inteiro("ID da vaga: ")
    mostrar(buscar_registros_por_vaga(vaga_id))


def opcao_buscar_registro_data():
    data_hora_entrada = ler_texto("Data e hora de entrada (AAAA-MM-DD HH:MM:SS): ")
    mostrar(buscar_registros_por_data_entrada(data_hora_entrada))


def opcao_buscar_registros_abertos():
    print("\nRegistros em aberto:")
    mostrar(buscar_registros_em_aberto())


def opcao_atualizar_registro():
    id_registro = ler_inteiro("ID do registro: ")
    data_hora_entrada = ler_texto("Nova data e hora de entrada (AAAA-MM-DD HH:MM:SS): ")
    data_hora_saida = ler_texto("Data e hora de saída (Enter se ainda estiver estacionado): ")
    veiculo_id = ler_inteiro("Novo ID do veículo: ")
    vaga_id = ler_inteiro("Novo ID da vaga: ")

    if data_hora_saida == "":
        data_hora_saida = None

    if atualizar_registro(id_registro, data_hora_entrada, data_hora_saida, veiculo_id, vaga_id):
        print("Registro atualizado com sucesso.")
    else:
        print("Nenhum registro foi alterado. Confira o ID e os valores informados.")


def opcao_remover_registro():
    confirmar_remocao(remover_registro, "registro")


def menu_busca_registros():
    executar_menu(MENU_BUSCA_REGISTROS, ACOES_BUSCA_REGISTROS)


def menu_registros():
    executar_menu(MENU_REGISTROS, ACOES_REGISTROS)


def opcao_consultar_vagas_dispositivos():
    print("\nVagas e dispositivos (1:1):")
    mostrar(consultar_vagas_dispositivos())


def opcao_consultar_clientes_veiculos():
    print("\nClientes e veículos (1:N):")
    mostrar(consultar_clientes_veiculos())


def opcao_consultar_veiculos_vagas():
    print("\nVeículos e vagas (N:M):")
    mostrar(consultar_veiculos_vagas())


def menu_consultas():
    executar_menu(MENU_CONSULTAS, ACOES_CONSULTAS)


ACOES_BUSCA_CLIENTES = {
    "1": opcao_buscar_cliente_id,
    "2": opcao_buscar_cliente_nome,
    "3": opcao_buscar_cliente_cpf,
}

ACOES_CLIENTES = {
    "1": opcao_inserir_cliente,
    "2": opcao_listar_clientes,
    "3": menu_busca_clientes,
    "4": opcao_atualizar_cliente,
    "5": opcao_remover_cliente,
}

ACOES_BUSCA_VEICULOS = {
    "1": opcao_buscar_veiculo_id,
    "2": opcao_buscar_veiculo_placa,
    "3": opcao_buscar_veiculo_modelo,
    "4": opcao_buscar_veiculo_cliente,
}

ACOES_VEICULOS = {
    "1": opcao_inserir_veiculo,
    "2": opcao_listar_veiculos,
    "3": menu_busca_veiculos,
    "4": opcao_atualizar_veiculo,
    "5": opcao_remover_veiculo,
}

ACOES_BUSCA_SETORES = {
    "1": opcao_buscar_setor_id,
    "2": opcao_buscar_setor_nome,
    "3": opcao_buscar_setor_capacidade,
}

ACOES_SETORES = {
    "1": opcao_inserir_setor,
    "2": opcao_listar_setores,
    "3": menu_busca_setores,
    "4": opcao_atualizar_setor,
    "5": opcao_remover_setor,
}

ACOES_BUSCA_DISPOSITIVOS = {
    "1": opcao_buscar_dispositivo_id,
    "2": opcao_buscar_dispositivo_mac,
}

ACOES_DISPOSITIVOS = {
    "1": opcao_inserir_dispositivo,
    "2": opcao_listar_dispositivos,
    "3": menu_busca_dispositivos,
    "4": opcao_atualizar_dispositivo,
    "5": opcao_remover_dispositivo,
}

ACOES_BUSCA_VAGAS = {
    "1": opcao_buscar_vaga_id,
    "2": opcao_buscar_vaga_codigo,
    "3": opcao_buscar_vaga_ocupacao,
    "4": opcao_buscar_vaga_setor,
    "5": opcao_buscar_vaga_dispositivo,
}

ACOES_VAGAS = {
    "1": opcao_inserir_vaga,
    "2": opcao_listar_vagas,
    "3": menu_busca_vagas,
    "4": opcao_atualizar_vaga,
    "5": opcao_remover_vaga,
}

ACOES_BUSCA_REGISTROS = {
    "1": opcao_buscar_registro_id,
    "2": opcao_buscar_registro_veiculo,
    "3": opcao_buscar_registro_vaga,
    "4": opcao_buscar_registro_data,
    "5": opcao_buscar_registros_abertos,
}

ACOES_REGISTROS = {
    "1": opcao_inserir_registro,
    "2": opcao_listar_registros,
    "3": menu_busca_registros,
    "4": opcao_atualizar_registro,
    "5": opcao_remover_registro,
}

ACOES_CONSULTAS = {
    "1": opcao_consultar_vagas_dispositivos,
    "2": opcao_consultar_clientes_veiculos,
    "3": opcao_consultar_veiculos_vagas,
}

ACOES_PRINCIPAIS = {
    "1": menu_clientes,
    "2": menu_veiculos,
    "3": menu_setores,
    "4": menu_dispositivos,
    "5": menu_vagas,
    "6": menu_registros,
    "7": menu_consultas,
}
MENUS = (
    menu_clientes,
    menu_veiculos,
    menu_setores,
    menu_dispositivos,
    menu_vagas,
    menu_registros,
    menu_consultas,
    menu_busca_clientes,
    menu_busca_veiculos,
    menu_busca_setores,
    menu_busca_dispositivos,
    menu_busca_vagas,
    menu_busca_registros
)


def main():
    print("Sistema iniciado.")

    executar_menu(MENU_PRINCIPAL, ACOES_PRINCIPAIS)

    print("Até a próxima!")


if __name__ == "__main__":
    main()