📝 README Melhorado
API Flask - Gerenciamento de Tipos

Uma API REST desenvolvida com Flask, Flask-RESTx, SQLAlchemy e PostgreSQL para retornar informações de tipos com base no ID. Utiliza migrações com Alembic e segue uma estrutura modularizada para melhor organização e escalabilidade.
🚀 Tecnologias Utilizadas

    Python 3.x
    Flask (com Flask-RESTx para documentação)
    PostgreSQL (Banco de dados)
    SQLAlchemy + Alembic (ORM e migrações)
    Marshmallow (Serialização de dados)
    Dotenv (Carregamento de variáveis de ambiente)

✅ Fluxo Completo de Instalação e Execução
1️⃣ Clone o Repositório

git clone https://github.com/MykleBR/QuiteJ-.git

cd Api-flask

2️⃣ Criação e Ativação do Ambiente Virtual

python -m venv venv

venv\Scripts\activate  # Windows

3️⃣ Instalação das Dependências

pip install -r requirements.txt

4️⃣ Configuração do Banco de Dados

    Edite o arquivo .env (se existir) ou modifique app/main/config.py para garantir que as credenciais do banco de dados estão corretas.
    Certifique-se de que o PostgreSQL está rodando.
    Crie o banco de dados (se ainda não existir):

    CREATE DATABASE postgres;

5️⃣ Aplicar Migrações

alembic upgrade head

Esse comando cria as tabelas definidas no SQLAlchemy.
6️⃣ População do Banco de Dados

python populate_db.py

Esse script adiciona registros iniciais no banco.
7️⃣ Inicializar a API

python main.py

O servidor Flask iniciará na porta 5000.
8️⃣ Testar no Postman ou Navegador

    Endpoint: GET /api/tipo?id=1
    URL para Teste:

    http://127.0.0.1:5000/api/tipo?id=1


📚 Documentação Automática com Swagger

Com Flask-RESTx, você pode acessar a documentação da API de forma automática atraves do Swagger:

http://127.0.0.1:5000/api/ Swagger Ui

http://127.0.0.1:5000/api/swagger.json  Swagger JSON

Esse endpoint fornece uma interface interativa para testar os endpoints!
📌 Considerações Finais

    O projeto segue boas práticas de arquitetura com separação de responsabilidades.
    Utiliza Flask-RESTx para documentação integrada via Swagger.
    Banco de dados gerenciado via SQLAlchemy + Alembic para versionamento.
    Código modular e fácil de escalar.
