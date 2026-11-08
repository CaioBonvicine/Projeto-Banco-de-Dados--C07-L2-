USE mydb;

INSERT INTO Veiculo (placa, modelo, Cliente_id)
SELECT 'RST5U67', 'Volkswagen Polo', 1
FROM DUAL
WHERE NOT EXISTS (
    SELECT 1 FROM Veiculo
    WHERE placa = 'RST5U67'
);
INSERT INTO Registro_Estacionamento (data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id)
SELECT '2026-11-04 08:00:00', '2026-11-04 09:00:00', 1, 3
FROM DUAL
WHERE NOT EXISTS (
    SELECT 1 FROM Registro_Estacionamento
    WHERE data_hora_entrada = '2026-11-04 08:00:00'
    AND Veiculo_id = 1
    AND Vaga_id = 3
);

INSERT INTO Registro_Estacionamento (data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id)
SELECT '2026-11-05 09:00:00', '2026-11-05 10:30:00', 3, 1
FROM DUAL
WHERE NOT EXISTS (
    SELECT 1 FROM Registro_Estacionamento
    WHERE data_hora_entrada = '2026-11-05 09:00:00'
    AND Veiculo_id = 3
    AND Vaga_id = 1
);


SELECT
    Vaga.codigo AS vaga,
    Dispositivo.id AS id_dispositivo
FROM Vaga
INNER JOIN `Dispositovo_Detecção` AS Dispositivo
    ON Vaga.Dispositovo_Detecção_id = Dispositivo.id
ORDER BY Vaga.codigo;


SELECT
    Cliente.nome AS cliente,
    Veiculo.placa AS placa,
    Veiculo.modelo AS modelo
FROM Cliente
INNER JOIN Veiculo
    ON Cliente.id = Veiculo.Cliente_id
ORDER BY Cliente.nome;


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
ORDER BY Veiculo.placa, Registro_Estacionamento.data_hora_entrada;


SELECT
    Cliente.nome AS cliente,
    Veiculo.placa AS placa,
    Veiculo.modelo AS modelo,
    Vaga.codigo AS vaga,
    Setor.nome AS setor,
    Dispositivo.id AS id_dispositivo,
    Registro_Estacionamento.data_hora_entrada,
    Registro_Estacionamento.data_hora_saida
FROM Cliente
INNER JOIN Veiculo
    ON Cliente.id = Veiculo.Cliente_id
INNER JOIN Registro_Estacionamento
    ON Veiculo.id = Registro_Estacionamento.Veiculo_id
INNER JOIN Vaga
    ON Registro_Estacionamento.Vaga_id = Vaga.id
INNER JOIN Setor
    ON Vaga.Setor_id = Setor.id
INNER JOIN `Dispositovo_Detecção` AS Dispositivo
    ON Vaga.Dispositovo_Detecção_id = Dispositivo.id
ORDER BY Registro_Estacionamento.data_hora_entrada DESC;


SELECT
    Veiculo.id,
    Veiculo.placa,
    COUNT(DISTINCT Registro_Estacionamento.Vaga_id) AS quantidade_vagas
FROM Veiculo
INNER JOIN Registro_Estacionamento
    ON Veiculo.id = Registro_Estacionamento.Veiculo_id
GROUP BY Veiculo.id, Veiculo.placa
HAVING COUNT(DISTINCT Registro_Estacionamento.Vaga_id) > 1
ORDER BY quantidade_vagas DESC;