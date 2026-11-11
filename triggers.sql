USE mydb;

DROP TRIGGER IF EXISTS placa_maiuscula;
DROP TRIGGER IF EXISTS ocupar_vaga;
DROP TRIGGER IF EXISTS capacidade_setor;

DELIMITER $$

-- Antes de cadastrar um veiculo, deixa a placa em letra maiuscula
CREATE TRIGGER placa_maiuscula
BEFORE INSERT ON Veiculo
FOR EACH ROW
BEGIN
    SET NEW.placa = UPPER(NEW.placa);
END $$

-- Depois de registrar uma entrada, marca a vaga como ocupada
CREATE TRIGGER ocupar_vaga
AFTER INSERT ON Registro_Estacionamento
FOR EACH ROW
BEGIN
    IF NEW.data_hora_saida IS NULL THEN
        UPDATE Vaga SET `ocupação` = 1 WHERE id = NEW.Vaga_id;
    END IF;
END $$

-- Antes de cadastrar um setor, nao deixa a capacidade ficar negativa
CREATE TRIGGER capacidade_setor
BEFORE INSERT ON Setor
FOR EACH ROW
BEGIN
    IF NEW.capacidade_maxima < 0 THEN
        SET NEW.capacidade_maxima = 0;
    END IF;
END $$

DELIMITER ;

-- Testes
INSERT INTO Veiculo (placa, modelo, Cliente_id) VALUES ('xyz9a87', 'Fiat Mobi', 2);
SELECT * FROM Veiculo WHERE modelo = 'Fiat Mobi';

INSERT INTO Setor (nome, capacidade_maxima) VALUES ('Setor Teste', -5);
SELECT * FROM Setor WHERE nome = 'Setor Teste';
