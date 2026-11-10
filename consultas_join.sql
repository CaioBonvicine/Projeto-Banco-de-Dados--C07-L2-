USE mydb;

-- Dados adicionais para demonstrar os relacionamentos
INSERT INTO Veiculo
(placa, modelo, Cliente_id)
VALUES
('RST5U67', 'Volkswagen Polo', 1);

INSERT INTO Registro_Estacionamento
(data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id)
VALUES
('2026-11-04 08:00:00', '2026-11-04 09:00:00', 1, 3),
('2026-11-05 09:00:00', '2026-11-05 10:30:00', 3, 1);


-- Relacionamento 1:1 (Vaga e Dispositivo)
SELECT
    Vaga.codigo AS vaga,
    Dispositivo.id AS id_dispositivo
FROM Vaga
INNER JOIN `Dispositovo_Detecção` AS Dispositivo
    ON Vaga.Dispositovo_Detecção_id = Dispositivo.id
ORDER BY Vaga.codigo;


-- Relacionamento 1:N (Cliente e Veiculo)
SELECT
    Cliente.nome AS cliente,
    Veiculo.placa AS placa,
    Veiculo.modelo AS modelo
FROM Cliente
INNER JOIN Veiculo
    ON Cliente.id = Veiculo.Cliente_id
ORDER BY Cliente.nome;


-- Relacionamento N:M (Veiculo e Vaga)
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


-- Consulta completa das informacoes do estacionamento
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


-- Veiculos com mais de um registro de estacionamento
SELECT
    Veiculo.id,
    Veiculo.placa,
    COUNT(Registro_Estacionamento.Vaga_id) AS quantidade_registros
FROM Veiculo
INNER JOIN Registro_Estacionamento
    ON Veiculo.id = Registro_Estacionamento.Veiculo_id
GROUP BY Veiculo.id, Veiculo.placa
HAVING COUNT(Registro_Estacionamento.Vaga_id) > 1
ORDER BY quantidade_registros DESC;