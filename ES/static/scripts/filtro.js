document.addEventListener('DOMContentLoaded', () => {
    const filtersForm = document.getElementById('filters-form');
    const projectCards = document.querySelectorAll('.project-card');

    if (filtersForm) {
        filtersForm.addEventListener('submit', (e) => {
            e.preventDefault();
            applyFilters();
        });
    }

    function applyFilters() {
        const searchTerm = document.getElementById('search').value.toLowerCase();
        const selectedSkill = document.getElementById('habilidade').value;
        const selectedLocation = document.getElementById('localizacao').value;

        projectCards.forEach(card => {
            const projectTitle = card.querySelector('h3').textContent.toLowerCase();
            const projectLocation = card.querySelector('.project-card-location').textContent;
            
            const skillTags = card.querySelectorAll('.project-card-tags .tag');
            let cardHasSkill = false;
            
            skillTags.forEach(tag => {
                if (tag.dataset.skill === selectedSkill) {
                    cardHasSkill = true;
                }
            });

            const matchesSearch = projectTitle.includes(searchTerm);
            const matchesLocation = (selectedLocation === 'all') || (projectLocation === selectedLocation);
            const matchesSkill = (selectedSkill === 'all') || cardHasSkill;

            if (matchesSearch && matchesLocation && matchesSkill) {
                card.style.display = 'flex'; 
            } else {
                card.style.display = 'none';
            }
        });
    }
});