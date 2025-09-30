const showLoginBtn = document.getElementById('showLoginBtn');
const showRegisterBtn = document.getElementById('showRegisterBtn');
const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');

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

showLoginBtn.addEventListener('click', showLoginForm);
showRegisterBtn.addEventListener('click', showRegisterForm);

document.addEventListener('DOMContentLoaded', function() {
    const hash = window.location.hash;

    if (hash === '#register') {
        showRegisterForm();
    } else {
        showLoginForm();
    }
});