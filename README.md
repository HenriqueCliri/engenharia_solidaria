# Engenharia Solidária 🏗️

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Plataforma web desenvolvida como projeto acadêmico para conectar estudantes de engenharia a projetos de construção e reforma em comunidades, permitindo a aplicação prática do conhecimento em ações de impacto social.

---

### Índice

- [1. Sobre o Projeto](#1-sobre-o-projeto)
- [2. Contexto Acadêmico](#2-contexto-acadêmico)
- [3. Funcionalidades](#3-funcionalidades)
- [4. Tecnologias Utilizadas](#4-tecnologias-utilizadas)
- [5. Como Executar](#5-como-executar)
- [6. Estrutura de Arquivos](#6-estrutura-de-arquivos)
- [7. Autores](#7-autores)

---

### 1. Sobre o Projeto

O "Engenharia Solidária" ataca duas frentes principais:
* **Para os estudantes:** Vivenciar e ter experiências, aplicando os conhecimentos teóricos adquiridos em sala de aula.
* **Para a comunidade:** A falta de acesso a apoio técnico qualificado para realizar pequenas construções, reformas e reparos essenciais.

Nossa plataforma web serve como uma ponte, criando um ecossistema onde estudantes podem ganhar experiência de campo enquanto contribuem para resolver problemas reais de pessoas que vivem em situações críticas.

### 2. Contexto Acadêmico

Este projeto é parte integrante da avaliação da disciplina extensionista **LÓGICA DE PROGRAMAÇÃO EM PYTHON**, do semestre letivo 2025.2, no Centro Universitário Fanor Wyden – UniFanor. O desenvolvimento segue as políticas institucionais de integração entre ensino e extensão, com foco em criar soluções de tecnologia com relevância social, viabilidade técnica e baixo custo.

- **Instituição:** Centro Universitário Fanor Wyden – UniFanor
- **Professor Orientador:** Prof. Juvenaldo Florentino Canja

### 3. Funcionalidades

O protótipo atual (front-end) conta com três páginas principais:

- **Página Inicial (`index.html`):**
    - Apresentação do propósito do projeto.
    - Seção "Como Funciona" para orientar novos usuários.
    - Destaque para projetos que necessitam de voluntários.

- **Página de Projetos (`projetos.html`):**
    - Listagem completa de todos os projetos disponíveis em formato de cards.
    - Funcionalidade de **busca por nome** e **filtro por habilidade técnica**.

- **Página de Detalhes do Projeto (`detalhes-projeto.html`):**
    - Visão aprofundada de um projeto específico.
    - Informações sobre descrição, habilidades necessárias, vagas e responsáveis.
    - Botão de ação principal para o voluntário se inscrever na ação.

### 4. Tecnologias Utilizadas

As seguintes tecnologias foram empregadas no desenvolvimento do front-end do projeto:

- **`HTML5`:** Estruturação e semântica do conteúdo.
- **`CSS3`:** Estilização, layout responsivo (Flexbox e Grid) e design moderno.
- **`JavaScript`:** Manipulação do DOM para interatividade dos filtros na página de projetos.
Excelente! Planejar os próximos passos é crucial para a evolução do projeto. Criar uma "To-Do List" (lista de tarefas) ajuda a organizar o desenvolvimento e a dividir o trabalho entre a equipe.

Aqui está uma To-Do List detalhada para as futuras funcionalidades, dividida por módulos, como você sugeriu. Você pode adicionar isso ao seu `README.md` ou usar como um guia de desenvolvimento para o grupo.

---

### **✅ To-Do List: Próximos Passos do "Engenharia Solidária"**

Esta lista detalha as funcionalidades planejadas para transformar o protótipo atual em uma plataforma completa e funcional. ;)

---

#### **Módulo 1: Autenticação e Perfis de Usuário (Back-end e Front-end)**

-   [ ] **1.1. Modelagem do Banco de Dados:**
    -   [ ] Criar a tabela `Usuarios` (com campos para nome, email, senha criptografada, curso, semestre, tipo de usuário - ex: 'estudante', 'parceiro').
    -   [ ] Criar a tabela `Habilidades` (para armazenar as competências técnicas, ex: 'Elétrica', 'AutoCAD').
    -   [ ] Criar uma tabela de associação `Usuario_Habilidades` para conectar usuários a múltiplas habilidades.

-   [ ] **1.2. Desenvolvimento do Back-end (Python/Flask):**
    -   [ ] Criar a rota e a lógica para o **cadastro de novos usuários**, incluindo a validação de dados e a criptografia da senha.
    -   [ ] Implementar o sistema de **login**, com validação de credenciais e criação de sessão de usuário.
    -   [ ] Desenvolver a funcionalidade de **logout**.
    -   [ ] Criar uma rota segura para a **edição do perfil** do usuário (atualizar nome, curso, habilidades, etc.).

-   [ ] **1.3. Desenvolvimento do Front-end:**
    -   [ ] Criar a **Página de Cadastro (`cadastro.html`)** com um formulário para coletar os dados do novo usuário.
    -   [ ] Criar a **Página de Login (`login.html`)** com campos para email e senha.
    -   [ ] Desenvolver a **Página de Perfil do Usuário**, onde ele poderá ver e editar suas informações.
    -   [ ] Adicionar lógica no menu de navegação para exibir "Login/Cadastro" para visitantes e "Meu Perfil/Sair" para usuários logados.

---

#### **Módulo 2: Gestão de Projetos e Parceiros (Back-end e Front-end)**

-   [ ] **2.2. Desenvolvimento do Back-end (Python/Flask):**
    -   [ ] Criar rotas seguras (apenas para parceiros logados) para **criar, editar e excluir projetos**.
    -   [ ] Desenvolver a lógica para que um estudante possa **se inscrever em um projeto**.
    -   [ ] Implementar a funcionalidade para o parceiro **visualizar e aprovar os voluntários** inscritos em seus projetos.
    -   [ ] Fazer com que as páginas de listagem e detalhes de projetos busquem os dados diretamente do banco de dados.

-   [ ] **2.3. Desenvolvimento do Front-end:**
    -   [ ] Criar um **Painel de Controle para o Parceiro**, onde ele possa gerenciar seus projetos e voluntários.
    -   [ ] Desenvolver o formulário de **criação e edição de projetos**.
    -   [ ] Adicionar um botão de "Inscrever-se" funcional na página de detalhes do projeto, que só aparece para estudantes logados.

---

#### **Módulo 3: Infraestrutura e Banco de Dados**

-   [ ] **3.1. Escolha do Banco de Dados:**
    -   [ ] Iniciar o desenvolvimento com **SQLite** por ser simples e já vir integrado ao Flask.

A disciplina tem como foco a **Lógica de Programação em Python**, portanto, o plano para futuras versões é desenvolver
