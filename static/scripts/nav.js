// Arquivo: nav.js (VERSÃO FINAL E CORRIGIDA)

document.addEventListener('DOMContentLoaded', function() {
    const navAuthLinks = document.getElementById('nav-auth-links');
    const registerBtn = document.getElementById('btn-register');
    const bodyData = document.body.dataset;

    const isLoggedIn = bodyData.loggedIn === 'True';

    const urlProjetos = bodyData.urlProjetos;
    const urlParceiros = bodyData.urlParceiros;
    const urlSobreNos = bodyData.urlSobreNos;
    const urlLogin = bodyData.urlLogin;
    const urlRegister = bodyData.urlRegister;
    const urlLogout = bodyData.urlLogout;

    if (isLoggedIn) {
        navAuthLinks.innerHTML = `
            <a href="#">Meu Perfil</a>
            <a href="${urlProjetos}">Projetos</a>

            <a href="${urlLogout}">Sair</a>  `;
        
        if (registerBtn) {
            registerBtn.style.display = 'none';
        }

    } else {
        navAuthLinks.innerHTML = `
            <a href="${urlProjetos}">Projetos</a>
            <a href="${urlParceiros}">Parceiros</a>
            <a href="${urlSobreNos}">Sobre Nós</a>
            <a href="${urlLogin}">Login</a>
        `;

        if (registerBtn) {
            registerBtn.style.display = 'inline-block';
            registerBtn.href = urlRegister;
        }
    }
});