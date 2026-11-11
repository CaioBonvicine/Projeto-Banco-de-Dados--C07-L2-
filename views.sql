USE mydb;

DROP VIEW IF EXISTS vw_vagas_livres;
DROP VIEW IF EXISTS vw_clientes_veiculos;
DROP VIEW IF EXISTS vw_veiculos_estacionados;

-- Mostra as vagas livres e o setor de cada uma
CREATE VIEW vw_vagas_livres AS
SELECT Vaga.codigo, Setor.nome AS setor
FROM Vaga
INNER JOIN Setor ON Vaga.Setor_id = Setor.id
WHERE Vaga.`ocupação` = 0;

-- Mostra os clientes e seus veiculos
CREATE VIEW vw_clientes_veiculos AS
SELECT Cliente.nome, Cliente.telefone, Veiculo.placa, Veiculo.modelo
FROM Cliente
INNER JOIN Veiculo ON Cliente.id = Veiculo.Cliente_id;

-- Mostra os veiculos que ainda estao no estacionamento (sem saida)
CREATE VIEW vw_veiculos_estacionados AS
SELECT Veiculo.placa, Vaga.codigo AS vaga, Registro_Estacionamento.data_hora_entrada
FROM Registro_Estacionamento
INNER JOIN Veiculo ON Registro_Estacionamento.Veiculo_id = Veiculo.id
INNER JOIN Vaga ON Registro_Estacionamento.Vaga_id = Vaga.id
WHERE Registro_Estacionamento.data_hora_saida IS NULL;

-- Testes
SELECT * FROM vw_vagas_livres;
SELECT * FROM vw_clientes_veiculos;
SELECT * FROM vw_veiculos_estacionados;
