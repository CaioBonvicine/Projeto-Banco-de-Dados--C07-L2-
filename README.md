# Sistema Inteligente de Estacionamento

## 👥 Integrantes do Grupo

- **Caio Pereira Bonvicine**
- **Gabriel Brandão Fonseca Borges**
- **Raphael Ferreira de Oliveira**

## 🎯 Tema Escolhido

**Sistema Inteligente de Gerenciamento e Monitoramento de Estacionamento**

## 📝 Descrição do Tema

O projeto consiste na modelagem e implementação de um banco de dados para um sistema inteligente de gerenciamento e monitoramento de estacionamento.

O sistema permite o cadastro de clientes e seus respectivos veículos. A estrutura do estacionamento é organizada por setores, que agrupam as vagas disponíveis.

Para o monitoramento da ocupação, cada vaga possui um dispositivo de detecção exclusivo, representado no banco de dados por seu endereço MAC. A situação de cada vaga é armazenada por meio do atributo `ocupação`, indicando se está livre ou ocupada.

O histórico de utilização do estacionamento é armazenado na tabela `Registro_Estacionamento`, que relaciona os veículos às vagas utilizadas, registrando as datas e os horários de entrada e saída.

---

## 🗄️ Modelagem do Banco de Dados

O modelo relacional foi desenvolvido no **MySQL Workbench** e possui seis tabelas: `Cliente`, `Veiculo`, `Setor`, `Vaga`, `Dispositovo_Detecção` e `Registro_Estacionamento`.

### 1. Entidades e Atributos

**Cliente**

Armazena os dados dos clientes cadastrados no estacionamento.

- `id` (INT) - Chave primária, com incremento automático.
- `nome` (VARCHAR(100)) - Nome completo do cliente.
- `cpf` (CHAR(11)) - CPF do cliente, único e obrigatório.
- `telefone` (VARCHAR(20)) - Telefone de contato.

**Veiculo**

Armazena os veículos pertencentes aos clientes.

- `id` (INT) - Chave primária, com incremento automático.
- `placa` (CHAR(7)) - Placa do veículo, única e obrigatória.
- `modelo` (VARCHAR(45)) - Modelo do veículo.
- `Cliente_id` (INT) - Chave estrangeira que relaciona o veículo ao seu cliente.

**Setor**

Representa a divisão das áreas do estacionamento.

- `id` (INT) - Chave primária, com incremento automático.
- `nome` (VARCHAR(45)) - Nome ou identificação do setor.
- `capacidade_maxima` (INT) - Quantidade máxima de vagas suportadas pelo setor.

**Vaga**

Armazena as informações das vagas disponíveis no estacionamento.

- `id` (INT) - Chave primária, com incremento automático.
- `codigo` (VARCHAR(10)) - Código de identificação da vaga.
- `ocupação` (TINYINT) - Situação da vaga: 0 = livre; 1 = ocupada.
- `Setor_id` (INT) - Chave estrangeira que relaciona a vaga ao seu setor.
- `Dispositovo_Detecção_id` (INT) - Chave estrangeira que relaciona a vaga ao seu dispositivo de detecção.

**Dispositovo_Detecção**

Representa os dispositivos de detecção instalados nas vagas.

- `id` (INT) - Chave primária, com incremento automático.
- `endereço_mac` (CHAR(17)) - Endereço MAC do dispositivo, único e obrigatório.

**Registro_Estacionamento**

Armazena o histórico de utilização das vagas pelos veículos. Essa tabela é responsável por representar o relacionamento N:M entre veículos e vagas.

- `id` (INT) - Chave primária, com incremento automático.
- `data_hora_entrada` (DATETIME) - Data e horário de entrada do veículo.
- `data_hora_saida` (DATETIME) - Data e horário de saída do veículo, podendo permanecer NULL enquanto o veículo estiver estacionado.
- `Veiculo_id` (INT) - Chave estrangeira que identifica o veículo.
- `Vaga_id` (INT) - Chave estrangeira que identifica a vaga utilizada.

---

## 🔗 Mapeamento dos Relacionamentos

### 1. Relacionamentos 1:N (Um para Muitos)

**Cliente → Veiculo**

Um cliente pode possuir vários veículos cadastrados, mas cada veículo pertence a apenas um cliente. O relacionamento é estabelecido pela chave estrangeira `Cliente_id` na tabela `Veiculo`.

**Setor → Vaga**

Um setor pode possuir várias vagas, mas cada vaga pertence a apenas um setor. O relacionamento é estabelecido pela chave estrangeira `Setor_id` na tabela `Vaga`.

### 2. Relacionamento 1:1 (Um para Um)

**Vaga ↔ Dispositovo_Detecção**

Cada vaga possui um dispositivo de detecção associado, e cada dispositivo pode estar relacionado a apenas uma vaga.

Esse relacionamento é implementado pela chave estrangeira `Dispositovo_Detecção_id` na tabela `Vaga`, que possui uma restrição `UNIQUE`, impedindo que o mesmo dispositivo seja associado a mais de uma vaga.

### 3. Relacionamento N:M (Muitos para Muitos)

**Veiculo ↔ Vaga**

Um veículo pode utilizar diferentes vagas ao longo do tempo, assim como uma vaga pode receber diferentes veículos em momentos distintos.

Esse relacionamento é resolvido por meio da tabela intermediária `Registro_Estacionamento`, que possui as chaves estrangeiras `Veiculo_id` e `Vaga_id`, além dos atributos `data_hora_entrada` e `data_hora_saida`.

---

## 📁 Arquivos do Repositório

**`Modelo_Projeto(C07)_Estacionamento.mwb`**

Arquivo do modelo relacional desenvolvido no MySQL Workbench, contendo as tabelas, os atributos, as chaves primárias, as chaves estrangeiras e os relacionamentos do banco de dados.

**`script_projeto.sql`**

Script gerado automaticamente pelo **MySQL Workbench**, a partir do modelo relacional desenvolvido na ferramenta.

A geração foi realizada utilizando a opção **File → Export → Forward Engineer SQL CREATE Script**, que permite gerar o código SQL de criação do banco de dados com base na estrutura definida no modelo EER.

Dessa forma, o script é produzido automaticamente pelo próprio MySQL Workbench, incluindo a criação das tabelas, chaves primárias, chaves estrangeiras, índices e restrições de unicidade configuradas no modelo.

O arquivo também contém os comandos necessários para criar o banco de dados `mydb`.

**Atenção:** o script utiliza `DROP SCHEMA IF EXISTS mydb`, portanto sua execução remove o banco de dados `mydb` existente, incluindo suas tabelas e seus dados, antes de recriá-lo.

**`inserir_dados.sql`**

Script responsável por inserir os dados iniciais do projeto.

São inseridos, no mínimo, cinco registros em cada uma das seis tabelas:

- Cliente;
- Veiculo;
- Setor;
- Dispositovo_Detecção;
- Vaga;
- Registro_Estacionamento.

**`manipulacao_dados.sql`**

Script utilizado para demonstrar comandos de manipulação de dados (DML), por meio de `INSERT`, `UPDATE` e `DELETE`.

As operações simulam situações comuns do funcionamento de um estacionamento e permitem verificar as alterações realizadas nas tabelas.

**1. Registro da saída de um veículo (UPDATE)**

Inicialmente, o script atualiza o registro de estacionamento de ID 2, preenchendo sua data e horário de saída com `2026-11-03 12:00:00`.

Esse registro corresponde ao veículo de ID 2, que estava utilizando a vaga B-01 (ID 2).

Em seguida, a coluna `ocupação` da vaga de ID 2 é atualizada para `0`, indicando que a vaga foi liberada.

Dois comandos `SELECT` são executados para verificar as alterações:

- A consulta em `Registro_Estacionamento` apresenta a saída registrada do veículo.
- A consulta em `Vaga` confirma que a vaga B-01 passou a apresentar ocupação igual a `0` (livre).

**2. Inserção de um registro inconsistente (INSERT)**

O script realiza uma inserção propositalmente incorreta na tabela `Registro_Estacionamento`.

O registro utiliza os seguintes dados:

- Data e horário de entrada: `2026-12-04 13:00:00`.
- Data e horário de saída: `2026-11-03 13:05:00`.
- Veículo: ID 5.
- Vaga: ID 5.

O registro é inconsistente porque a data de saída é anterior à data de entrada.

Após a inserção, um comando `SELECT` consulta o registro pela data de entrada, permitindo verificar que os dados foram armazenados.

**3. Exclusão do registro inconsistente (DELETE)**

Depois de verificar o registro incorreto, o script utiliza `DELETE` para removê-lo da tabela `Registro_Estacionamento`.

A exclusão utiliza as informações do próprio registro para identificar exatamente a linha que deve ser removida.

Um último `SELECT` consulta novamente a data de entrada utilizada na inserção. Como o registro foi excluído, a consulta não retorna resultados.

As operações são realizadas dentro de uma transação, iniciada por `START TRANSACTION` e finalizada com `COMMIT`. Dessa forma, as alterações válidas são confirmadas, enquanto o registro inconsistente é removido antes da confirmação.

**`usuarios_roles.sql`**

Script responsável pela criação de dois usuários e de uma ROLE, chamada `role_estacionamento`, para organizar as permissões de acesso ao banco de dados.

As permissões compartilhadas pela ROLE são:

- `SELECT` em todas as tabelas do banco `mydb`.
- `INSERT` na tabela `Registro_Estacionamento`.
- `UPDATE` somente na coluna `data_hora_saida` da tabela `Registro_Estacionamento`.
- `UPDATE` somente na coluna `ocupação` da tabela `Vaga`.

Os usuários criados são:

- **usuario_operador:** recebe as permissões definidas pela ROLE `role_estacionamento`.
- **usuario_supervisor:** recebe as permissões da mesma ROLE e também todas as permissões disponíveis no escopo do banco de dados `mydb`.

A ROLE é concedida aos dois usuários e configurada como padrão para suas conexões locais (`localhost`).

**`consultas_join.sql`**

Script responsável por realizar consultas utilizando `INNER JOIN`, demonstrando os três tipos de relacionamentos presentes no modelo: 1:1, 1:N e N:M.

Antes das consultas, são inseridos dados adicionais para ampliar os resultados e demonstrar melhor os relacionamentos:

- Um veículo Volkswagen Polo, de placa `RST5U67`, associado ao cliente de ID 1 (Ana Souza).
- Um registro de estacionamento do veículo de ID 1 na vaga de ID 3, correspondente à vaga VIP-01, em `2026-11-04`.
- Um registro de estacionamento do veículo de ID 3 na vaga de ID 1, correspondente à vaga A-01, em `2026-11-05`.

Essas inserções complementam os dados iniciais e permitem demonstrar situações em que um cliente possui mais de um veículo e em que um veículo utiliza diferentes vagas ao longo do tempo.

### Consultas realizadas

**1. Relacionamento 1:1 — Vaga e Dispositivo**

A primeira consulta relaciona as tabelas `Vaga` e `Dispositovo_Detecção`, utilizando a chave estrangeira `Dispositovo_Detecção_id`.

O resultado apresenta o código de cada vaga e o ID do dispositivo de detecção associado.

São retornadas cinco linhas, correspondentes às cinco vagas cadastradas:

- A-01 → Dispositivo 1.
- B-01 → Dispositivo 2.
- C-01 → Dispositivo 4.
- D-01 → Dispositivo 5.
- VIP-01 → Dispositivo 3.

Essa consulta demonstra que cada vaga está associada a um dispositivo exclusivo.

**2. Relacionamento 1:N — Cliente e Veículo**

A segunda consulta relaciona `Cliente` e `Veiculo` por meio da chave estrangeira `Cliente_id`.

O resultado apresenta o nome do cliente, a placa e o modelo de cada veículo cadastrado.

São retornadas seis linhas, pois o cliente Ana Souza possui dois veículos, enquanto os outros quatro clientes possuem um veículo cada.

O resultado demonstra que um mesmo cliente pode estar relacionado a vários veículos.

**3. Relacionamento N:M — Veículo e Vaga**

A terceira consulta relaciona `Veiculo`, `Registro_Estacionamento` e `Vaga`.

A tabela `Registro_Estacionamento` funciona como intermediária, permitindo identificar quais veículos utilizaram quais vagas ao longo do tempo.

O resultado apresenta a placa e o modelo do veículo, o código da vaga utilizada e as datas e horários de entrada e saída.

São retornadas sete linhas, correspondentes aos sete registros de estacionamento existentes.

Um mesmo veículo pode aparecer mais de uma vez, pois cada linha representa uma utilização de vaga em determinado momento.

Esse resultado demonstra o relacionamento N:M entre veículos e vagas.

**4. Consulta completa das informações do estacionamento**

A quarta consulta reúne as seis tabelas do banco de dados:

- `Cliente`;
- `Veiculo`;
- `Registro_Estacionamento`;
- `Vaga`;
- `Setor`;
- `Dispositovo_Detecção`.

O resultado apresenta, para cada registro de estacionamento, o nome do cliente, a placa e o modelo do veículo, o código da vaga, o setor, o ID do dispositivo de detecção e as datas e horários de entrada e saída.

São retornadas sete linhas, uma para cada registro de estacionamento.

Essa consulta permite visualizar em conjunto as principais informações relacionadas à utilização do estacionamento.

**5. Veículos com mais de um registro de estacionamento**

A última consulta utiliza `COUNT`, `GROUP BY` e `HAVING` para agrupar os registros de estacionamento por veículo e identificar aqueles que possuem mais de um registro.

O resultado apresenta o ID do veículo, sua placa e a quantidade de registros de estacionamento encontrados.

Com os dados cadastrados, são retornados dois veículos:

- ABC1D23: 2 registros de estacionamento.
- GHI7J89: 2 registros de estacionamento.

Os demais veículos possuem apenas um registro cada e, por isso, não aparecem no resultado.

Essa consulta demonstra como utilizar agrupamentos e condições sobre os grupos para identificar veículos com maior histórico de utilização do estacionamento.

---

## ▶️ Ordem de Execução dos Scripts

Para configurar o banco de dados a partir do zero, recomenda-se executar os arquivos na seguinte ordem:

1. `script_projeto.sql` — cria o banco de dados e as tabelas.
2. `inserir_dados.sql` — insere os registros iniciais.
3. `manipulacao_dados.sql` — demonstra as operações de manipulação de dados.
4. `consultas_join.sql` — adiciona os dados complementares e executa as consultas com JOIN.
5. `usuarios_roles.sql` — cria os usuários, a ROLE e configura as permissões.

**Importante:** o arquivo `script_projeto.sql` deve ser executado somente quando houver intenção de reconstruir o banco do zero, pois ele remove o banco `mydb` existente antes de criá-lo novamente.

O arquivo consultas_join.sql também deve ser executado apenas uma vez após a inserção dos dados iniciais, pois adiciona registros complementares ao banco.

---