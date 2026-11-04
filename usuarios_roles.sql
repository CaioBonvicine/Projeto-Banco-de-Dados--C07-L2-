USE mydb;
DROP USER IF EXISTS 'usuario_operador'@'localhost', 'usuario_supervisor'@'localhost';
DROP ROLE IF EXISTS 'role_estacionamento';
CREATE ROLE 'role_estacionamento';

GRANT SELECT ON mydb.* TO 'role_estacionamento';
GRANT INSERT ON mydb.Registro_Estacionamento TO 'role_estacionamento';
GRANT UPDATE (data_hora_saida) ON mydb.Registro_Estacionamento TO 'role_estacionamento';
GRANT UPDATE (`ocupação`) ON mydb.Vaga TO 'role_estacionamento';

CREATE USER 'usuario_operador'@'localhost' IDENTIFIED BY 'Teste_Operador#2026';
CREATE USER 'usuario_supervisor'@'localhost' IDENTIFIED BY 'Teste_Supervisor#2026';

GRANT 'role_estacionamento' TO 'usuario_operador'@'localhost', 'usuario_supervisor'@'localhost';

SET DEFAULT ROLE 'role_estacionamento' TO 'usuario_operador'@'localhost', 'usuario_supervisor'@'localhost';

GRANT ALL PRIVILEGES ON mydb.* TO 'usuario_supervisor'@'localhost';

SHOW GRANTS FOR 'role_estacionamento';
SHOW GRANTS FOR 'usuario_operador'@'localhost' USING 'role_estacionamento';
SHOW GRANTS FOR 'usuario_supervisor'@'localhost' USING 'role_estacionamento';