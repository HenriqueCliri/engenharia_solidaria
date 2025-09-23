        const filtroPesquisa = document.getElementById('search');
        const filtroHabilidade = document.getElementById('habilidade');
        const todosOsProjetos = document.querySelectorAll('.project-card');

        function aplicarFiltros() {
            const termoPesquisa = filtroPesquisa.value.toLowerCase();
            const habilidadeSelecionada = filtroHabilidade.value; // Já está em minúsculas pelo HTML

            todosOsProjetos.forEach(function(card) {
                const tituloCard = card.querySelector('h3').textContent.toLowerCase();
                const tagsDoCard = card.querySelectorAll('.tag');

                // Condição 1: Pesquisa
                const matchPesquisa = tituloCard.includes(termoPesquisa);

                // Condição 2: Habilidade
                let matchHabilidade = false;
                if (habilidadeSelecionada === "") { // "Todas"
                    matchHabilidade = true;
                } else {
                    tagsDoCard.forEach(function(tag) {
                        // A MUDANÇA ESTÁ AQUI:
                        // Verificamos se 'data-skill' existe e comparamos
                        if (tag.dataset.skill && tag.dataset.skill === habilidadeSelecionada) {
                            matchHabilidade = true;
                        }
                    });
                }

                // Exibe o card somente se ambas as condições forem verdadeiras
                if (matchPesquisa && matchHabilidade) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }

        filtroPesquisa.addEventListener('keyup', aplicarFiltros);
        filtroHabilidade.addEventListener('change', aplicarFiltros);