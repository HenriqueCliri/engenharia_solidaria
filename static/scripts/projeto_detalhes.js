// Arquivo: projeto-detalhes.js
document.addEventListener('DOMContentLoaded', function() {
    const btnInscrever = document.getElementById('btn-inscrever');

    btnInscrever.addEventListener('click', function(event) {    
        event.preventDefault(); // Impede o link de navegar para "#"

        const isLoggedIn = localStorage.getItem('isLoggedIn');

        if (isLoggedIn === 'true') {
            // Se o usuário estiver logado, redireciona para a página de confirmação
            window.location.href = 'confirmacao_inscricao.html';
        } else {
            // Se não estiver logado, avisa e redireciona para o login
            alert('Você precisa estar logado para se inscrever em um projeto.');
            window.location.href = 'login_cadastro.html#login';
        }
    });
});