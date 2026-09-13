# Sistema Inteligente de Estacionamento

## 👥 Integrantes do Grupo
* **Caio Pereira Bonvicine**
* **Gabriel Brandão Fonseca Borges**
* **Raphael Ferreira de Oliveira**

## 🎯 Tema Escolhido
**Sistema Inteligente de Gerenciamento e Monitoramento de Estacionamento**

## 📝 Descrição do Tema
O projeto consiste na modelagem e desenvolvimento de um banco de dados para um sistema de estacionamento automatizado. O fluxo principal realiza o cadastro de clientes e seus respectivos veículos. A estrutura do pátio é dividida pela entidade Setor, responsável por agrupar as vagas disponíveis. 

Para a automação do espaço, cada vaga conta com um Dispositivo de Detecção (sensor IoT) exclusivo para monitorar a ocupação em tempo real. Por fim, o histórico de uso e movimentação do pátio é controlado por meio dos Registros de Estacionamento, que associam a utilização dos veículos às vagas ao longo do tempo.

---

## 🗄️ Modelagem do Banco de Dados

O modelo relacional foi estruturado no **MySQL Workbench** e conta com 6 entidades, atendendo aos requisitos de tipos de dados e relacionamentos exigidos:

### 1. Entidades e Atributos

* **Cliente**
  * `id_cliente` (INT) - Primary Key, Auto Increment
  * `nome` (VARCHAR(100)) - Nome completo do cliente
  * `cpf` (VARCHAR(11)) - CPF do cliente (Unique, Not Null)
  * `telefone` (VARCHAR(20)) - Telefone de contato

* **Veiculo**
  * `id_veiculo` (INT) - Primary Key, Auto Increment
  * `placa` (VARCHAR(10)) - Placa do veículo (Unique, Not Null)
  * `modelo` (VARCHAR(45)) - Modelo/marca do veículo

* **Setor**
  * `id_Setor` (INT) - Primary Key, Auto Increment
  * `Nome_setor` (VARCHAR(45)) - Nome ou identificação do setor (Ex: "Setor A", "Setor VIP")
  * `capacidade_maxima` (INT) - Quantidade limite de vagas suportadas no setor

* **Vaga**
  * `id_vaga` (INT) - Primary Key, Auto Increment
  * `codigo` (VARCHAR(10)) - Código identificador da vaga (Ex: "A-01")
  * `ocupação` (TINYINT) - Status da vaga (0 = livre, 1 = ocupada)

* **Dispositivo_Deteccao**
  * `id_Dispositivo` (INT) - Primary Key, Auto Increment
  * `endereço_mac` (VARCHAR(45)) - Endereço MAC do sensor IoT instalado (Unique, Not Null)

* **Registro_Estacionamento** *(Tabela Intermediária do relacionamento N:M)*
  * `id_Registro` (INT) - Primary Key, Auto Increment
  * `data_hora_entrada` (DATETIME) - Registra o momento de entrada do veículo
  * `data_hora_saida` (DATETIME) - Registra o momento de saída do veículo

---

### 🔗 Mapeamento dos Relacionamentos

1. **Relacionamentos 1:N (Um para Muitos):**
   * **Cliente ➔ Veiculo:** Um cliente pode ter mais de um veículo registrado, mas cada veículo está associado a apenas um cliente (`fk_cliente`).
   * **Setor ➔ Vaga:** Um setor contém/agrupa múltiplas vagas, mas cada vaga pertence a um único setor (`fk_setor`).

2. **Relacionamento 1:1 (Um para Um):**
   * **Vaga ➔ Dispositivo_Deteccao:** Cada vaga possui exatamente um dispositivo de detecção associado, e cada sensor monitora exclusivamente uma vaga (`fk_vaga` com restrição UNIQUE).

3. **Relacionamento N:M (Muitos para Muitos):**
   * **Veiculo ➔ Vaga:** Um mesmo veículo pode estacionar em diversas vagas ao longo do tempo, assim como uma vaga recebe diversos veículos diferentes.
   * **Tabela Intermediária:** Resolvido através da entidade **`Registro_Estacionamento`**, utilizando nome específico e legível, contendo as chaves estrangeiras `fk_veiculo` e `fk_vaga`, além de atributos próprios do evento de estacionar (`data_hora_entrada` e `data_hora_saida`).

---

## 📁 Arquivos do Repositório
* `Modelo_Projeto(C07)_Estacionamento.mwb`: Arquivo de modelagem gerado pelo MySQL Workbench.
* `README.md`: Documentação oficial com especificações e alinhamento do grupo.