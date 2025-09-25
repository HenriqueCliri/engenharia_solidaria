// Arquivo: auth.js

// 1. Pega todos os elementos necessários do HTML
const showLoginBtn = document.getElementById('showLoginBtn');
const showRegisterBtn = document.getElementById('showRegisterBtn');
const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');

// 2. Cria funções reutilizáveis para mostrar cada formulário
function showLoginForm() {
    loginForm.classList.remove('hidden');
    registerForm.classList.add('hidden');
    showLoginBtn.classList.add('active');
    showRegisterBtn.classList.remove('active');
}

function showRegisterForm() {
    registerForm.classList.remove('hidden');
    loginForm.classList.add('hidden');
    showRegisterBtn.classList.add('active');
    showLoginBtn.classList.remove('active');
}

// 3. Adiciona os "escutadores" para os cliques nos botões
showLoginBtn.addEventListener('click', showLoginForm);
showRegisterBtn.addEventListener('click', showRegisterForm);

// 4. LÓGICA PRINCIPAL: Verifica a URL assim que a página carrega
document.addEventListener('DOMContentLoaded', function() {
    const hash = window.location.hash; // Pega a parte da URL após o '#'

    if (hash === '#register') {
        // Se a URL terminar com #register, mostra o formulário de cadastro
        showRegisterForm();
    } else {
        // Para qualquer outro caso (incluindo #login ou sem nada), mostra o de login
        showLoginForm();
    }
});