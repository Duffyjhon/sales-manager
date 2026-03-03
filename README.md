# 📊 Sales Manager — Sistema de Gestão de Vendas (Deploy em Produção)

Aplicação full stack desenvolvida com foco em backend, autenticação segura e banco de dados em produção.

🔗 **Aplicação online:**  
https://sales-manager-o4kb.onrender.com  

---

## 🎯 Objetivo do Projeto

Construir um sistema completo de gestão de vendas com:

- API REST estruturada
- Autenticação JWT
- Banco de dados relacional em produção
- Dashboard com métricas e crescimento mensal
- Exportação de relatórios (PDF e Excel)
- Deploy em ambiente cloud

O projeto foi desenvolvido como estudo prático focado em arquitetura backend e resolução de problemas reais em ambiente de produção.

---

## 🚀 Principais Funcionalidades

🔐 Autenticação segura com JWT  
📊 Dashboard com:
- Total de vendas
- Valor total
- Valor médio
- Crescimento percentual mensal
- Melhor mês de faturamento  

💰 CRUD completo de vendas  
🔎 Filtro e busca dinâmica  
📤 Exportação para Excel (.xlsx)  
📄 Exportação para PDF (.pdf)  
🌙 Tema escuro persistente  

---

## 🧠 Desafios Técnicos Resolvidos

- Migração de SQLite (ambiente local) para PostgreSQL (produção)
- Tratamento de erros HTTP (400, 401, 405)
- Configuração de variáveis de ambiente no Render
- Agrupamento de vendas por mês no backend
- Formatação monetária em padrão brasileiro (BRL)
- Organização em camadas (models, routes, services)

---

## 🧰 Tecnologias Utilizadas

### Backend
- Python
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- PostgreSQL (produção)
- SQLite (fallback local)
- Gunicorn
- ReportLab (PDF)
- OpenPyXL (Excel)

### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla JS)
- Chart.js
- Font Awesome

---

## 🧪 Credenciais para Teste

Usuário padrão (caso já criado):

Usuário: admin  
Senha: 123456  

Se necessário, crie o usuário acessando uma vez:
```
/setup/create-admin
```

⚠️ Observação: Em ambiente real de produção, esse endpoint deve ser removido ou protegido.

---

## 🗄️ Banco de Dados

- Produção (Render): PostgreSQL via variável `DATABASE_URL`
- Ambiente local: SQLite automático se `DATABASE_URL` não estiver definida

---

## 🚀 Como Rodar Localmente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Duffyjhon/sales-manager.git
cd sales-manager
```

### 2️⃣ Criar ambiente virtual

```bash
python -m venv .venv
```

### 3️⃣ Ativar ambiente virtual

Windows (PowerShell):
```bash
.\.venv\Scripts\Activate.ps1
```

Windows (CMD):
```bash
.\.venv\Scripts\activate.bat
```

Linux/macOS:
```bash
source .venv/bin/activate
```

### 4️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 5️⃣ Executar aplicação

```bash
python run.py
```

Acesse:
```
http://127.0.0.1:5000
```

---

## ☁️ Deploy no Render

Web Service (Python)

Build Command:
```
pip install -r requirements.txt
```

Start Command:
```
gunicorn "backend.myapp:create_app()" --bind 0.0.0.0:$PORT
```

Variáveis de ambiente necessárias:
- DATABASE_URL
- SECRET_KEY
- JWT_SECRET_KEY

---

## 📂 Estrutura do Projeto

```
sales-manager/
├── backend/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── config.py
│   └── myapp.py
├── frontend/
│   ├── login.html
│   ├── dashboard.html
│   ├── vendas.html
│   ├── styles/
│   └── js/
├── migrations/
├── requirements.txt
└── README.md
```

---

## 🛣️ Melhorias Futuras

- Remover/proteger `/setup/create-admin`
- Testes automatizados
- Controle de permissões (admin/usuário)
- CI/CD
- Dockerização

---

## 👨‍💻 Autor

João Vitor Mendonça  
GitHub: https://github.com/Duffyjhon

---

## 📄 Licença

MIT
