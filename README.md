# Engenharia Solidária 🏗️

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Plataforma web desenvolvida como projeto acadêmico para conectar estudantes de engenharia a projetos de construção e reforma em comunidades, permitindo a aplicação prática do conhecimento em ações de impacto social.

---

### Índice

- [1. Sobre o Projeto](#1-sobre-o-projeto)
- [2. Contexto Acadêmico](#2-contexto-acadêmico)
- [3. Tecnologias Utilizadas](#3-tecnologias-utilizadas)
- [4. Como Executar](#4-como-executar)
- [5. Estrutura de Arquivos](#5-estrutura-de-arquivos)
- [6. Autores](#6-autores)

---

### 1. Sobre o Projeto

O "Engenharia Solidária" ataca duas frentes principais:
* **Para os estudantes:** Vivenciar e ter experiências, aplicando os conhecimentos teóricos adquiridos em sala de aula.
* **Para a comunidade:** A falta de acesso a apoio técnico qualificado para realizar pequenas construções, reformas e reparos essenciais.

Nossa plataforma web serve como uma ponte, criando um ecossistema onde estudantes podem ganhar experiência de campo enquanto contribuem para resolver problemas reais de pessoas que vivem em situações críticas.

### 2. Contexto Acadêmico

Este projeto é parte integrante da avaliação da disciplina extensionista **LÓGICA DE PROGRAMAÇÃO**, do semestre letivo 2025.2, no Centro Universitário Fanor Wyden – UniFanor. O desenvolvimento segue as políticas institucionais de integração entre ensino e extensão, com foco em criar soluções de tecnologia com relevância social, viabilidade técnica e baixo custo.

- **Instituição:** Centro Universitário Fanor Wyden – UniFanor
- **Professor Orientador:** Prof. Juvenaldo Florentino Canja

### 3. Tecnologias Utilizadas

As seguintes tecnologias utilizada:

- **`HTML5`:** Estruturação e semântica do conteúdo.
- **`CSS3`:** Estilização, layout responsivo (Flexbox e Grid) e design moderno.
- **`JavaScript`:** Manipulação do DOM para interatividade dos filtros na página de projetos.
- **`Python3`** Servidor para executar de forma local.
- **`Flask`** (Mricroframework web)
- **`Flask-SQLAlchemy`** (ORM para integração com o banco de dados)
- **`Werkzeug`** (Para criptografia de senhas)
- **`SQLite`** (Banco de dados)
- **`Venv`** (Ambiente virtual python)

A disciplina tem como foco a **Lógica de Programação**, portanto, o plano para futuras versões é desenvolver

### 4. Como Executar

O projeto utiliza um servidor web local embutido no Python para servir os arquivos estáticos (HTML, CSS, JS). Para executá-lo, siga os passos abaixo:

#### a. **Pré-requisito:** 
- **Python 3**
- **Git**

#### b. **Passos da instalação**

1. **Clone ou baixe este repositório para o seu computador e extraia os arquivos em uma pasta.**

    ```bash
    git clone https://github.com/HenriqueCliri/engenharia_solidaria.git
    cd engenharia_solidaria
    ```

2. **Crie e ative o ambiente virtual (venv).**

    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows
    venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r Flask Flask-SQLAlchemy
    ```

4.  **Crie o banco de dados:**
    Execute o `flask shell` e os comandos para criar as tabelas e adicionar projetos de exemplo.
    
    ```bash
    # Inicia o shell do Flask
    flask shell

    # Dentro do shell (>>>), execute:
    from app import db
    db.create_all()

    from app import Project
    projeto1 = Project(title='Reforma da Creche Comunitária Sonhar', description='A creche precisa de uma reforma em suas instalações elétricas...', location='Bairro Bom Jardim, Fortaleza')
    projeto2 = Project(title='Construção de Horta na Escola Local', description='Vamos construir uma horta comunitária no pátio da escola...', location='Bairro Jangurussu, Fortaleza')
    db.session.add_all([projeto1, projeto2])
    db.session.commit()
    exit()
    ```

5.  Com o ambiente virtual ativo execute o seguinte comando para subir o servidor:

    ```bash
    flask run
    ```
 Abra seu navegador de internet e acesse a seguinte URL: **http://localhost:5000**
