
USE mydb;

DROP TRIGGER IF EXISTS liberar_vaga;

DELIMITER $$

-- Libera automaticamente a vaga quando o veiculo sai
CREATE TRIGGER liberar_vaga
AFTER UPDATE ON Registro_Estacionamento
FOR EACH ROW
BEGIN
    IF NEW.data_hora_saida IS NOT NULL
       AND OLD.data_hora_saida IS NULL THEN

        UPDATE Vaga
        SET `ocupação` = 0
        WHERE id = NEW.Vaga_id;

    END IF;
END $$

DELIMITER ;

-- Teste da Trigger liberar_vaga

START TRANSACTION;

-- Registra um veiculo na vaga 5
INSERT INTO Registro_Estacionamento
(data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id)
VALUES
(NOW(), NULL, 5, 5);

SET @registro_teste = LAST_INSERT_ID();

-- Define a vaga como ocupada para o teste
UPDATE Vaga
SET `ocupação` = 1
WHERE id = 5;

-- Verifica a vaga antes da saida
SELECT * FROM Vaga WHERE id = 5;

-- Registra a saida do veiculo
UPDATE Registro_Estacionamento
SET data_hora_saida = NOW()
WHERE id = @registro_teste;

-- Verifica se a vaga foi liberada
SELECT * FROM Vaga WHERE id = 5;

-- Desfaz as alteracoes realizadas no teste
ROLLBACK;
