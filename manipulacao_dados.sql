USE mydb;

START TRANSACTION;

-- Registra a saida de um veiculo
UPDATE Registro_Estacionamento SET data_hora_saida = '2026-11-03 12:00:00' WHERE id = 2;

-- Libera a vaga utilizada pelo veiculo
UPDATE Vaga SET ocupação = 0 WHERE id = 2;


SELECT * FROM Registro_Estacionamento WHERE id = 2;
SELECT * FROM Vaga WHERE codigo = 'B-01';


-- Cria registro incorreto (data de entrada no futuro e data de saida no passado)
INSERT INTO Registro_Estacionamento (data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id) VALUES ('2026-12-04 13:00:00', '2026-11-03 13:05:00', 5, 5);

SELECT * FROM Registro_Estacionamento WHERE data_hora_entrada = '2026-12-04 13:00:00';

-- Exclui registro incorreto
DELETE FROM Registro_Estacionamento WHERE data_hora_entrada = '2026-12-04 13:00:00' AND data_hora_saida = '2026-11-03 13:05:00' AND Veiculo_id = 5 AND Vaga_id = 5;

SELECT * FROM Registro_Estacionamento WHERE data_hora_entrada = '2026-12-04 13:00:00';


COMMIT;