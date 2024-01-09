"# sinobras" 
Introdução
Este software é desenvolvido para gerenciar e avaliar a qualidade de lotes de aço, seguindo normas específicas.
O objetivo é automatizar a avaliação da qualidade, garantindo conformidade com as normas NBR 7480 e outras aplicáveis.

Requisitos do Sistema
Requisitos de Hardware:

CPU: Processador de 1GHz ou superior.
Memória: Mínimo de 2GB RAM.
Armazenamento: 10GB de espaço disponível.
Requisitos de Software:

Sistema Operacional: Windows, Linux ou macOS.
Python: Versão 3.6 ou superior.
Django: Versão 3.x.x.
Banco de Dados: PostgreSQL, MySQL, SQLite ou outro compatível com Django.
Dependências:
As bibliotecas Python necessárias estão listadas no arquivo requirements.txt. Execute pip install -r requirements.txt para instalá-las.

Configuração e Instalação
Configuração do Ambiente de Desenvolvimento:

Instale o Python:

Certifique-se de ter o Python 3.6 ou superior instalado. Pode ser baixado de python.org.
Configuração do Ambiente Virtual:

Instale o virtualenv: pip install virtualenv.
Crie um ambiente virtual na raiz do projeto: virtualenv venv.
Ative o ambiente virtual (source venv/bin/activate no Linux/macOS ou venv\Scripts\activate no Windows).
Instalação de Dependências:

Instale as dependências do projeto: pip install -r requirements.txt.
Instalação do Software:

Clone o Repositório:

Clone o repositório do projeto do GitHub.
Configuração do Banco de Dados:

Instale e configure o banco de dados de sua escolha (PostgreSQL, MySQL, SQLite, etc.).
Crie um novo banco de dados para o projeto.
Configure as credenciais do banco de dados no arquivo de configuração do Django (settings.py).
Migrações do Django:

Execute python manage.py migrate para criar as tabelas no banco de dados.
Executar o Servidor de Desenvolvimento:

Execute python manage.py runserver para iniciar o servidor de desenvolvimento.
Acesse o aplicativo em http://localhost:8000.