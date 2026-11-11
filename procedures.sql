USE mydb;

DROP PROCEDURE IF EXISTS sp_cadastrar_cliente;
DROP PROCEDURE IF EXISTS sp_registrar_entrada;
DROP PROCEDURE IF EXISTS sp_registrar_saida;

DELIMITER $$

-- Cadastra um novo cliente
CREATE PROCEDURE sp_cadastrar_cliente(IN nome_cliente VARCHAR(100), IN cpf_cliente CHAR(11), IN telefone_cliente VARCHAR(20))
BEGIN
    INSERT INTO Cliente (nome, cpf, telefone)
    VALUES (nome_cliente, cpf_cliente, telefone_cliente);
END $$

-- Registra a entrada de um veiculo em uma vaga
CREATE PROCEDURE sp_registrar_entrada(IN veiculo INT, IN vaga INT)
BEGIN
    INSERT INTO Registro_Estacionamento (data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id)
    VALUES (NOW(), NULL, veiculo, vaga);
END $$

-- Registra a saida de um veiculo e libera a vaga
CREATE PROCEDURE sp_registrar_saida(IN registro INT, IN vaga INT)
BEGIN
    UPDATE Registro_Estacionamento SET data_hora_saida = NOW() WHERE id = registro;
    UPDATE Vaga SET `ocupação` = 0 WHERE id = vaga;
END $$

DELIMITER ;

-- Testes
CALL sp_cadastrar_cliente('Fernanda Rocha', '66666666666', '35999990006');
SELECT * FROM Cliente WHERE cpf = '66666666666';

CALL sp_registrar_entrada(1, 1);
SELECT * FROM vw_veiculos_estacionados;

CALL sp_registrar_saida(4, 4);
SELECT * FROM Registro_Estacionamento WHERE id = 4;
