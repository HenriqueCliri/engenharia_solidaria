document.addEventListener('DOMContentLoaded', function() {
    const btnInscrever = document.getElementById('btn-inscrever');

    if (btnInscrever) {

        btnInscrever.addEventListener('click', function(event) {    
            event.preventDefault();

            const isLoggedIn = document.body.dataset.loggedIn === 'True';

            const urlConfirmacao = document.body.dataset.urlConfirmacao;
            const urlLogin = document.body.dataset.urlLogin;

            if (isLoggedIn) {
                window.location.href = urlConfirmacao;
            } else {
                window.location.href = urlLogin + '#login';
            }
        });
    } else {
        console.error("Erro ao se inscrever!")
    }
});