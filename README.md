# 🛒 Sales Manager — Sistema de Gestão de Vendas

Sistema web para gerenciamento de vendas com autenticação JWT, dashboard interativo e exportação de dados.

🔗 **Aplicação online (Render):**  
https://sales-manager-o4kb.onrender.com

---

## ✨ Funcionalidades

- 🔐 Login com JWT
- 📊 Dashboard com métricas
- 💰 Cadastro de vendas
- 🔎 Filtro e busca de vendas
- ❌ Exclusão de vendas
- 📤 Exportação para Excel (.xlsx)
- 📄 Exportação para PDF (.pdf)
- 🌙 Tema escuro com persistência

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
