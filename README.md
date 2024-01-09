# Sinobras

## Introdução
Este software é desenvolvido para gerenciar e avaliar a qualidade de lotes de aço, seguindo normas específicas. O objetivo é automatizar a avaliação da qualidade, garantindo conformidade com as normas NBR 7480 e outras aplicáveis.

## Requisitos do Sistema
**Requisitos de Hardware**:
- CPU: Processador de 1GHz ou superior.
- Memória: Mínimo de 2GB RAM.
- Armazenamento: 10GB de espaço disponível.

**Requisitos de Software**:
- Sistema Operacional: Windows, Linux ou macOS.
- Python: Versão 3.6 ou superior.
- Django: Versão 3.x.x.
- Banco de Dados: PostgreSQL, MySQL, SQLite ou outro compatível com Django.

**Dependências**:
- As bibliotecas Python necessárias estão listadas no arquivo `requirements.txt`. Execute `pip install -r requirements.txt` para instalá-las.

## Configuração e Instalação
**Configuração do Ambiente de Desenvolvimento**:
1. Instale o Python.
2. Instale o virtualenv e configure um ambiente virtual.
3. Ative o ambiente virtual e instale as dependências.

**Instalação do Software**:
1. Clone o repositório do projeto.
2. Configure o banco de dados.
3. Execute as migrações do Django.
4. Inicie o servidor de desenvolvimento e acesse a aplicação.
## Executando Migrações no Django

Antes de iniciar o servidor pela primeira vez, é necessário aplicar as migrações do Django para configurar o banco de dados.

1. **Abra o Terminal ou Prompt de Comando**:
   - Certifique-se de que você está no diretório do seu projeto Django.

2. **Ative o Ambiente Virtual (se estiver usando um)**:
   - No Windows: `venv\Scripts\activate`.
   - No Linux ou macOS: `source venv/bin/activate`.

3. **Execute as Migrações**:
   - Digite `python manage.py makemigrations` e pressione Enter.
   - Digite `python manage.py migrate` e pressione Enter.

Essas migrações configuram o banco de dados com as tabelas necessárias para o funcionamento do Django e do seu projeto.
## Acesso ao Sistema
Faça login usando suas credenciais de usuário.

## Gerenciamento de Lotes de Aço
### Criação de Lotes
- Navegue até a aba 'Lotes'.
- Clique em 'Criar Novo Lote'.
- Preencha os detalhes necessários e salve.

### Edição e Exclusão de Lotes
- Acesse 'Lotes' para visualizar a lista de lotes existentes.
- Escolha um lote para editar ou excluir conforme necessário.

## Realização e Registro de Ensaios Mecânicos
### Adicionar Ensaio ao Lote
- Na página de detalhes do lote, clique em 'Adicionar Ensaio Mecânico'.
- Insira todos os resultados dos ensaios realizados.

### Avaliação Automática do Lote
- O sistema avalia automaticamente o lote com base nos resultados dos ensaios.
- Verifique o status de avaliação na página de detalhes do lote.
