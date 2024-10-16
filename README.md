<h1 align="center"> Desafio back-end - EJECT </h1>

![Imagem de capa - desafio back-end](https://github.com/user-attachments/assets/783fa8ed-2a88-4a6b-9a75-2feaa1775df2)

Este projeto consiste no desenvolvimento do back-end de uma plataforma educacional, que gerencia recursos e ferramentas voltadas para a educação. O projeto foi desenvolvido como parte do processo seletivo da Empresa Júnior da Escola de Ciências e Tecnologia da UFRN (EJECT).  

## 🔧 Funcionalidades do Projeto

O sistema back-end oferece suporte às seguintes funcionalidades:

-  **Gerenciamento de usuários:** Cadastro, autenticação e controle de permissões para alunos, professores e pais.
-  **Administração de conteúdos:** Criação, edição e remoção de vídeos, posts no fórum e materiais de apoio educacional.
-  **Gerenciamento de comentários:** Controle de postagens e interações no fórum.
-  **Dashboard de controle:** Interface para administradores acompanharem o desempenho da plataforma.

## 🚀 Tecnologias Utilizadas

O back-end foi construído utilizando as seguintes tecnologias:

-  **Django:** Framework principal para criação da aplicação web, gerenciamento de banco de dados e sistema de autenticação.
-  **SQLite:** Banco de dados para armazenar informações dos usuários e conteúdo.

## 📁 Estrutura do Projeto

A estrutura básica do projeto está organizada da seguinte forma:

>     ├── core/               # Contém a lógica principal do projeto
>     │   ├── models.py       # Modelos de dados (vídeos, comentários, usuários, etc.)
>     │   ├── views.py        # Views que gerenciam as requisições HTTP
>     │   └── urls.py         # Definição das rotas/endpoints da API
>     ├── templates/          # Templates HTML para renderização (caso necessário)
>     ├── static/             # Arquivos estáticos (CSS, imagens, etc.)
>     ├── utilis.py           # Funções auxiliares e utilitárias
>     └── manage.py           # Arquivo de gerenciamento do Django

### Principais Modelos  

-  **Home:**
-  **Tool:** Modelo que armazena informações sobre as principais funcionalidades e ferramentas da plataforma exibidas na página inicial.
-  **Team:** Modelo que representa os membros da equipe, com detalhes como nome, função e descrição exibidos na página inicial.

-  **Vídeos:**
-  **Video:** Modelo que armazena informações sobre os vídeos educativos, incluindo título, descrição, link do vídeo e a categoria correspondente.

-  **Fórum:**
-  **Post:** Modelo que armazena as postagens no fórum, incluindo campos como título, conteúdo, momento exato e o autor da postagem.
-  **Comment:** Modelo para gerenciar os comentários feitos em cada post, associando-os ao respectivo **Post** e ao autor do comentário.

-  **Parents (Pais e Profs):**
-  **Material:** Modelo para armazenar materiais educativos voltados para pais e professores, incluindo campos como título, descrição, e link para download.

-  **Footer:**
-  **Contact:** Modelo para gerenciar informações de contato, como e-mails, telefones e links.
-  **Information:** Modelo para armazenar detalhes adicionais, como links úteis e informações gerais exibidas no rodapé.

## 🛠 Como Rodar o Projeto  

1. Clone o repositório:

`git clone https://github.com/rodrigofnobrega/desafio-eject-back-end.git`

2. Entre no diretório:

`cd desafio-eject-back-end`

3. Crie a venv:

`python -m venv ./venv`
`source venv/bin/activate`

4. Instale as dependências:

`pip install -r requirements.txt`

5. Aplique as migrações:

`python manage.py migrate`

6. Crie um superusuário:

`python manage.py createsuperuser`

7. Execute o servidor de desenvolvimento:

`python manage.py runserver`

8. Acesse o projeto:

`http://127.0.0.1:8000/`

## ✔️ Testes

Para rodar os testes, utilize o comando:

`python manage.py test`

## 🧑‍💻Autores

| <img src="https://github.com/rodrigofnobrega.png" alt="Rodrigo Nobrega" width="100" height="100"/> **[Rodrigo Nobrega](https://github.com/rodrigofnobrega)** | <img src="https://github.com/VitorBurratto.png" alt="Vítor Burratto" width="100" height="100"/> **[Vítor Burratto](https://github.com/VitorBurratto)**|
|--|--|
