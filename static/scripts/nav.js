// Arquivo: nav.js (VERSÃO ATUALIZADA)

document.addEventListener('DOMContentLoaded', function() {
    const isLoggedIn = localStorage.getItem('isLoggedIn');
    const navAuthLinks = document.getElementById('nav-auth-links');
    const registerBtn = document.getElementById('btn-register');

    // 1. Lê as URLs corretas que o Flask colocou nos atributos data-* do body
    const bodyData = document.body.dataset;
    const urlProjetos = bodyData.urlProjetos;
    const urlParceiros = bodyData.urlParceiros;
    const urlSobreNos = bodyData.urlSobreNos;
    const urlLogin = bodyData.urlLogin;
    
    // Links para quando o usuário está logado (perfil ainda é um placeholder)
    const urlPerfil = '#'; // Futuramente, pode ser /perfil
    const urlLogout = '#'; // O logout é tratado pelo evento de clique

    if (isLoggedIn === 'true') {
        // --- CONSTRÓI O HTML COM AS URLs CORRETAS ---
        // Usuário está logado: mostra link de Perfil e Sair
        navAuthLinks.innerHTML = `
            <a href="${urlPerfil}">Meu Perfil</a>
            <a href="#" id="logoutBtn">Sair</a>
        `;
        
        if (registerBtn) {
            registerBtn.style.display = 'none'; // Esconde o botão de cadastro
        }

        const logoutBtn = document.getElementById('logoutBtn');
        logoutBtn.addEventListener('click', function(event) {
            event.preventDefault();
            localStorage.removeItem('isLoggedIn');
            alert('Você saiu da sua conta.');
            // Redireciona para a página inicial usando a URL correta
            window.location.href = bodyData.urlHome;
        });

    } else {
        navAuthLinks.innerHTML = `
            <a href="${urlProjetos}">Projetos</a>
            <a href="${urlParceiros}">Parceiros</a>
            <a href="${urlSobreNos}">Sobre Nós</a>
            <a href="${urlLogin}">Login de Estudante</a>
        `;

        if (registerBtn) {
            registerBtn.style.display = 'inline-block';
            // Atualiza o botão de cadastro também
            registerBtn.href = bodyData.urlRegister;
        }
    }
});