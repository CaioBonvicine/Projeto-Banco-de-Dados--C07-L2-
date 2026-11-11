USE mydb;

DROP FUNCTION IF EXISTS fn_tempo_permanencia;
DROP FUNCTION IF EXISTS fn_valor_estacionamento;
DROP FUNCTION IF EXISTS fn_vagas_livres_setor;

DELIMITER $$

-- Retorna quantos minutos o veiculo ficou estacionado
CREATE FUNCTION fn_tempo_permanencia(entrada DATETIME, saida DATETIME)
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN TIMESTAMPDIFF(MINUTE, entrada, saida);
END $$

-- Retorna o valor a pagar (R$ 10,00 por hora)
CREATE FUNCTION fn_valor_estacionamento(entrada DATETIME, saida DATETIME)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    RETURN (TIMESTAMPDIFF(HOUR, entrada, saida) + 1) * 10.00;
END $$

-- Retorna quantas vagas livres um setor possui
CREATE FUNCTION fn_vagas_livres_setor(setor INT)
RETURNS INT
READS SQL DATA
BEGIN
    DECLARE total INT;

    SELECT COUNT(*) INTO total
    FROM Vaga
    WHERE Setor_id = setor AND `ocupação` = 0;

    RETURN total;
END $$

DELIMITER ;

-- Testes
SELECT fn_tempo_permanencia('2026-11-02 08:00:00', '2026-11-02 09:30:00');
SELECT fn_valor_estacionamento('2026-11-02 08:00:00', '2026-11-02 09:30:00');
SELECT fn_vagas_livres_setor(1);
