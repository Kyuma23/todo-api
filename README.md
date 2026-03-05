<div align="center">
  <h1>⚙️ TaskManager API</h1>
  <h3>API RESTful com FastAPI, PostgreSQL e Docker</h3>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
    <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
    <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="CI/CD" />
  </p>
</div>

<br>

## 🎯 Sobre o Projeto
Uma API RESTful desenvolvida com foco em **Clean Architecture** e boas práticas de Engenharia de Software. O sistema permite a gestão completa de tarefas (To-Do) e demonstra a integração fluida entre validação rigorosa de dados, ORM moderno e conteinerização.

### ✨ Funcionalidades Principais
- **CRUD Completo:** Criação, leitura, atualização e eliminação de tarefas.
- **Validação Rigorosa:** Modelos validados automaticamente via Pydantic e SQLModel.
- **Testes Unitários:** Suite de testes com `pytest`, utilizando *Dependency Override* para simular uma base de dados SQLite em memória durante os testes.
- **Infraestrutura as Code:** Ambiente de desenvolvimento e produção 100% isolado através de `docker-compose`.
- **CI/CD:** Pipeline automática no GitHub Actions que bloqueia código não funcional.

---

## 🚀 Como Executar (Via Docker)

A forma mais fácil de correr a aplicação é utilizando o Docker. Não precisas de instalar o Python nem o Postgres na tua máquina.

**1. Clona o repositório e entra na pasta:**
```bash
git clone [https://github.com/Kyuma23/todo-api](https://github.com/Kyuma23/todo-api)
cd todo-api
```

**2. Levanta a infraestrutura (API + Base de Dados):**
```bash
docker-compose up --build
```

**3. Acede à Documentação Automática:**
Abre o teu browser e vai a: [http://localhost:8000/docs](http://localhost:8000/docs)
*(O FastAPI gera uma interface Swagger UI automática para testares as rotas diretamente no browser).*

---

## 🧪 Como Correr os Testes Localmente

Se quiseres desenvolver localmente e correr a suite de testes:

```bash
# Ativar ambiente virtual e instalar dependências
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Correr o Pytest garantindo que o Python reconhece a raiz do projeto
PYTHONPATH=. pytest
```

---

## 📂 Estrutura de Diretórios (Arquitetura)

```text
├── src/
│   ├── main.py          # Ponto de entrada (Uvicorn / Lifespan)
│   ├── db.py            # Configuração do SQLModel e Motor Postgres
│   ├── routers/
│   │   └── todo.py      # Lógica de rotas (Endpoints)
│   └── test_main.py     # Suite de testes unitários
├── docker-compose.yml   # Orquestração de Containers
├── Dockerfile           # Imagem da API Python
└── requirements.txt     # Dependências do projeto
```

<div align="center">
  <br>
  <i>Desenvolvido com ☕ e Python por Diogo © 2026</i>
</div>