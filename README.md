<div align="center">
  <h1>⚙️ MyTodo Full-Stack Ecosystem</h1>
  <h3>API RESTful (FastAPI) + Frontend Reativo (Nuxt 3)</h3>
  
  <p>
    <img src="https://img.shields.io/badge/Nuxt_3-00DC82?style=for-the-badge&logo=nuxt.js&logoColor=white" alt="Nuxt 3" />
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
    <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
    <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="CI/CD" />
  </p>
</div>

<br>

## 🎯 Sobre o Projeto
Uma aplicação Full-Stack desenvolvida com foco em **Clean Architecture** e boas práticas de Engenharia de Software. O sistema integra um backend robusto em Python para gestão de tarefas (To-Do) com uma interface moderna e reativa em Nuxt 3, demonstrando a integração fluida entre validação rigorosa de dados, ORM moderno, interfaces de utilizador dinâmicas e conteinerização.

### ✨ Funcionalidades Principais
- **Interface Kanban Reativa:** Gestão visual de tarefas com colunas de estado (A Fazer / Concluído) filtradas dinamicamente e UX otimizada.
- **CRUD Completo:** Criação, leitura, atualização e eliminação de tarefas via API e UI.
- **Validação Rigorosa:** Modelos de dados validados automaticamente via Pydantic e SQLModel no backend.
- **Testes Unitários:** Suite de testes com `pytest`, utilizando *Dependency Override* para simular uma base de dados SQLite em memória durante os testes.
- **Infraestrutura as Code:** Ambiente de desenvolvimento e produção 100% isolado através de `docker-compose`.
- **CI/CD:** Pipeline automática no GitHub Actions que bloqueia código não funcional.

---

## 🚀 Como Executar (Via Docker)

A forma mais fácil de correr a aplicação completa é utilizando o Docker Compose.

**1. Clona o repositório e entra na pasta:**
```bash
git clone [https://github.com/Kyuma23/todo-api](https://github.com/Kyuma23/todo-api)
cd todo-api
```

**2. Levanta a infraestrutura completa (Frontend + Backend + DB):**
```bash
docker-compose up --build
```

**3. Acede às interfaces:**
- **Frontend (Web App):** [http://localhost:3000](http://localhost:3000)
- **Documentação API (Swagger UI):** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Como Correr os Testes Localmente

Se quiseres desenvolver localmente no backend e correr a suite de testes:

```bash
# Entrar na pasta do backend
cd backend

# Ativar ambiente virtual e instalar dependências
python -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt

# Correr o Pytest garantindo que o Python reconhece a raiz do projeto
PYTHONPATH=. pytest
```

---

## 📂 Estrutura de Diretórios (Arquitetura)

```text
.
├── docker-compose.yml       # Orquestração de containers (Rede & Volumes)
├── backend/                 # 🧠 SERVIÇO: API (FastAPI + SQLModel)
│   ├── main.py              # Ponto de entrada e Middleware CORS
│   ├── db.py                # Configuração da DB e Engine
│   ├── routers/
│   │   └── todo.py          # Endpoints da API (Lógica de rotas)
│   └── test_main.py         # Suite de testes unitários
├── frontend/                # 🎨 SERVIÇO: UI (Nuxt 3 + Tailwind)
│   ├── app.vue              # Ponto de entrada do Vue (NuxtPage)
│   ├── pages/
│   │   └── index.vue        # Dashboard Kanban e lógica de consumo
│   ├── components/
│   │   ├── KanbanHeader.vue # Formulário de entrada expansível
│   │   └── TaskCard.vue     # Componente visual da tarefa
│   ├── nuxt.config.ts       # Configuração de módulos e runtime
│   └── Dockerfile           # Build de produção (Node 20-Alpine)
└── requirements.txt         # Dependências do projeto Python
```

<div align="center">
  <br>
  <i>Desenvolvido com ☕ por Diogo © 2026</i>
</div>