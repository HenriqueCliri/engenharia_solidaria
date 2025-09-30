
document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search');
    const skillSelect = document.getElementById('habilidade');
    const projectCards = document.querySelectorAll('.project-card');

    function filterProjects() {
        const searchTerm = searchInput.value.toLowerCase().trim();
        const selectedSkill = skillSelect.value;

        projectCards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            const tags = card.querySelectorAll('.project-card-tags .tag');

            const searchMatch = title.includes(searchTerm);

            let skillMatch = false;
            if (selectedSkill === "") {
                skillMatch = true;
            } else {
                tags.forEach(tag => {
                    if (tag.dataset.skill === selectedSkill) {
                        skillMatch = true;
                    }
                });
            }
            if (searchMatch && skillMatch) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    searchInput.addEventListener('keyup', filterProjects);
    skillSelect.addEventListener('change', filterProjects);
});