# site-de-bolo-Flask_SQL
site de bolo simples com python e sql
# 🍰 Loja de Bolos Delícia

Uma aplicação web simples feita com **Flask + SQLite** para simular uma loja de bolos. O usuário pode visualizar os produtos disponíveis e adicionar bolos ao carrinho de compras, que é salvo no banco de dados.

---

## 🛠️ Tecnologias utilizadas

- Python 3.x
- Flask
- SQLite
- HTML5 + CSS3
- JavaScript (Fetch API)

---

## 📂 Estrutura do projeto
loja_bolos/
├── app.py # Aplicação Flask principal
├── criar_banco.py # Script para criação do banco SQLite
├── database.db # Banco de dados SQLite (criado após rodar o script)
├── static/
│ ├── style.css # Estilo da página
│ └── script.js # Lógica para adicionar ao carrinho
├── templates/
│ └── index.html # Página inicial da loja
│ └── carrinho.html # (Opcional) Visualização do carrinho
└── README.md


Crie o ambiente virtual (opcional):

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows


💡 Funcionalidades
Exibe bolos com imagens, nome e preço.

Permite adicionar bolos ao carrinho (com banco SQLite).

(Opcional) Rota para visualizar o carrinho.

Estilo agradável com HTML e CSS.

Código organizado e separado em templates, static e banco de dados.

