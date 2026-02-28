# 💼 Sales Manager — Sistema de Gestão de Vendas

Sistema completo de gerenciamento de vendas com dashboard, autenticação JWT, relatórios e exportação em Excel e PDF.

---

## 🚀 Demonstração

Aplicação web com:

* 🔐 Login seguro com JWT
* 📊 Dashboard com estatísticas
* 🛒 Registro e listagem de vendas
* 🔎 Busca e filtro por produto
* 🗑️ Exclusão de vendas
* 📄 Exportação para Excel e PDF
* 🌙 Tema escuro
* 🎨 Interface moderna

---

## 🖥️ Tecnologias Utilizadas

### Backend

* Python 3
* Flask
* Flask-JWT-Extended
* Flask-SQLAlchemy
* Flask-Migrate
* SQLite
* ReportLab (PDF)
* OpenPyXL (Excel)

### Frontend

* HTML5
* CSS3
* JavaScript (Vanilla)
* Chart.js
* Font Awesome

---

## 📂 Estrutura do Projeto

```
sales-manager/
│
├── backend/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── schemas/
│   ├── utils/
│   ├── myapp.py
│   └── config.py
│
├── frontend/
│   ├── login.html
│   ├── dashboard.html
│   ├── vendas.html
│   ├── styles/
│   └── js/
│
├── migrations/
├── instance/
└── README.md
```

---

## ⚙️ Como executar localmente

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/Duffyjhon/sales-manager.git
cd sales-manager
```

---

### 2️⃣ Criar ambiente virtual

```bash
python -m venv .venv
```

Ativar:

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

---

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Executar o servidor

```bash
python backend/myapp.py
```

---

### 5️⃣ Acessar no navegador

```
http://127.0.0.1:5000
```

---

## 🔐 Autenticação

O sistema utiliza tokens JWT para proteger rotas da API.

Após login, o token é armazenado no navegador e usado nas requisições.

---

## 📊 Funcionalidades

### ✔ Dashboard

* Total de vendas
* Valor total
* Valor médio
* Vendas por produto (gráfico)

### ✔ Gestão de vendas

* Registrar venda
* Listar vendas
* Buscar por cliente
* Filtrar por produto
* Excluir vendas

### ✔ Exportação

* Excel (.xlsx)
* PDF (.pdf)

---

## 🌙 Tema Escuro

O sistema possui modo dark com persistência de preferência.

---

## 🧠 Objetivo do Projeto

Projeto desenvolvido para prática de desenvolvimento full-stack com Flask e JavaScript puro, simulando um sistema real de uso empresarial.

---

## 👨‍💻 Autor

**João Vitor Mendonça**

GitHub:
👉 https://github.com/Duffyjhon

---

## ⭐ Licença

Este projeto é open source e pode ser usado para fins educacionais e portfólio.
