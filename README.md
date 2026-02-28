# todo-api

1. A Fundação (O Repositório)

[x]    Cria uma pasta nova chamada todo-api.

[x]   Inicia o Git, cria o .gitignore e o ambiente virtual (venv).

[x]   Instala o fastapi, uvicorn, e o sqlmodel.

[x]   Dica de Ouro: Vais precisar de instalar a biblioteca psycopg2-binary para o Python conseguir falar com o Postgres!

2. A Base de Dados (Docker)

[x]   Cria um ficheiro docker-compose.yml na raiz do projeto.

[x]   Configura um serviço usando a imagem oficial do postgres (versão 15 ou 16).

[x]   Define as variáveis de ambiente (User, Password, DB Name) e expõe a porta 5432.

[x]   Garante que o container levanta com docker compose up -d.

3. O Cérebro (A API)

[]   Cria a tua tabela SQLModel Tarefa (com id, titulo, descricao, e concluida como boolean).

[]   Configura o ficheiro da base de dados (o create_engine agora vai usar um URL do tipo postgresql://user:password@localhost:5432/dbname).

[]   Cria as rotas CRUD completas (POST para criar, GET para listar, PUT/PATCH para marcar como concluída, DELETE para apagar).

4. A Garantia de Qualidade (Pytest)

[]   Configura o teu test_main.py.

[]   Escreve no mínimo 2 testes (ex: criar uma tarefa e listar tarefas).

[]   Atenção: Lembra-te de fazer o override da base de dados nos testes, exatamente como fizeste no LegalEagle!

5. O Lançamento (Deploy no Render)

[]   Envia o teu código limpo para um novo repositório no GitHub.

[]   Cria uma conta no Render.com (usa o teu GitHub para login).

[]   Cria um "Web Service" ligado ao teu repositório e uma "PostgreSQL Database" gerida por eles (ambos no tier gratuito).

[]   Coloca as Variáveis de Ambiente (URL da Base de Dados) nas definições do Render.