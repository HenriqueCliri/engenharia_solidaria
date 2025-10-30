
document.addEventListener('DOMContentLoaded', () => {
    const showLoginBtn = document.getElementById('showLoginBtn');
    const showRegisterBtn = document.getElementById('showRegisterBtn');
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');

    function showLogin() {
        loginForm.classList.remove('hidden');
        registerForm.classList.add('hidden');
        showLoginBtn.classList.add('active');
        showRegisterBtn.classList.remove('active');
    }

    function showRegister() {
        loginForm.classList.add('hidden');
        registerForm.classList.remove('hidden');
        showLoginBtn.classList.remove('active');
        showRegisterBtn.classList.add('active');
    }

    if (showLoginBtn) {
        showLoginBtn.addEventListener('click', (e) => {
            e.preventDefault(); 
            showLogin();
        });
    }

    if (showRegisterBtn) {
        showRegisterBtn.addEventListener('click', (e) => {
            e.preventDefault();
            showRegister();
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', (e) => {
            const password = document.getElementById('registerPassword').value;
            const confirmPassword = document.getElementById('confirmPassword').value;

            if (password !== confirmPassword) {
                e.preventDefault(); 
                alert('As senhas não coincidem. Por favor, verifique.');
            }
        });
    }
    if (window.location.hash === '#register') {
        showRegister();
    } else {
        showLogin();
    }
});