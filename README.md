# Engenharia Solidária 🏗️

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Plataforma web desenvolvida como projeto acadêmico para conectar estudantes de engenharia a projetos de construção e reforma em comunidades, permitindo a aplicação prática do conhecimento em ações de impacto social.

---

### Índice

- [1. Sobre o Projeto](#1-sobre-o-projeto)
- [2. Contexto Acadêmico](#2-contexto-acadêmico)
- [3. Tecnologias Utilizadas](#3-tecnologias-utilizadas)
- [4. Como Executar](#4-como-executar)
- [5. Autores](#6-autores)

---

### 1. Sobre o Projeto

O "Engenharia Solidária" ataca duas frentes principais:
* **Para os estudantes:** Vivenciar e ter experiências, aplicando os conhecimentos teóricos adquiridos em sala de aula.
* **Para a comunidade:** Facilita o acesso a apoio técnico qualificado para realizar pequenas construções, reformas e reparos essenciais.

Nossa plataforma web serve como uma ponte, criando um ecossistema onde estudantes podem ganhar experiência de campo enquanto contribuem para resolver problemas reais no âmbito social.

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

A disciplina tem como foco a **Lógica de Programação**, portanto, o plano para futuras versões é desenvolver ainda mais a plataforma.

### 4. Como Executar

O projeto utiliza um servidor web local embutido no Python para servir os arquivos estáticos (HTML, CSS, JS). Para executá-lo, siga os passos abaixo:

#### a. **Pré-requisito:** 
- **Python3.x.x**
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
    python3 -m venv venv

    # Ativar no Windows
    venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install Flask Flask-SQLAlchemy
    ```

4.  Com o ambiente virtual ativo execute o seguinte comando para subir o servidor:

    ```bash
    python3 run.py
    ```
 Abra seu navegador de internet e acesse a seguinte URL: **http://localhost:5000**

### 5. Autores

- Davi
- Francisco Neto
- Ricardo
- Samya
- Henrique