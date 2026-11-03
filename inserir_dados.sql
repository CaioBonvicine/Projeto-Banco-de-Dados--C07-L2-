USE mydb;

START TRANSACTION;

INSERT INTO Cliente
(nome, cpf, telefone)
VALUES
('Ana Souza', '11111111111', '35999990001'),
('Bruno Lima', '22222222222', '35999990002'),
('Carla Mendes', '33333333333', '35999990003'),
('Daniel Alves', '44444444444', '35999990004'),
('Eduarda Costa', '55555555555', '35999990005');


INSERT INTO Setor
(nome, capacidade_maxima)
VALUES
('Setor A', 20),
('Setor B', 15),
('Setor VIP', 10),
('Setor Coberto', 25),
('Setor Visitantes', 15);

INSERT INTO Dispositovo_Detecção
(endereço_mac)
VALUES
('AA:BB:CC:DD:EE:01'),
('AA:BB:CC:DD:EE:02'),
('AA:BB:CC:DD:EE:03'),
('AA:BB:CC:DD:EE:04'),
('AA:BB:CC:DD:EE:05');

INSERT INTO Vaga
(codigo, ocupação, Setor_id, Dispositovo_Detecção_id)
VALUES
('A-01', 0, 1, 1),
('B-01', 1, 2, 2),
('VIP-01', 0, 3, 3),
('C-01', 1, 4, 4),
('D-01', 0, 5, 5);

INSERT INTO Veiculo
(placa, modelo, Cliente_id)
VALUES
('ABC1D23', 'Chevrolet Onix', 1),
('DEF4G56', 'Hyundai HB20', 2),
('GHI7J89', 'Toyota Corolla', 3),
('KLM1N23', 'Honda Civic', 4),
('OPQ4R56', 'Fiat Argo', 5);

INSERT INTO Registro_Estacionamento
(data_hora_entrada, data_hora_saida, Veiculo_id, Vaga_id)
VALUES
('2026-11-02 08:00:00', '2026-11-02 09:30:00', 1, 1),
('2026-11-03 08:00:00', NULL, 2, 2),
('2026-11-01 14:00:00', '2026-11-01 16:00:00', 3, 3),
('2026-11-03 09:00:00', NULL, 4, 4),
('2026-10-30 07:00:00', '2026-10-30 11:00:00', 5, 5);


COMMIT;