document.addEventListener('DOMContentLoaded', () => {
    const openMenu = document.getElementById('openMenu');
    const closeMenu = document.getElementById('closeMenu');
    const menu = document.getElementById('menu');

    openMenu.addEventListener('click', () => {
        menu.classList.add('open');
        openMenu.style.display = 'none';
    });

    closeMenu.addEventListener('click', () => {
        menu.classList.remove('open');
        openMenu.style.display = 'block';
    });

    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            menu.classList.remove('open');
            menu.removeAttribute('style');
            openMenu.style.display = 'none';
        } else {
            openMenu.style.display = 'block';
        }
    });
});

const searchInput = document.getElementById('search-bar');
const items = document.querySelectorAll('barinha');

// Adiciona um evento ao input que dispara toda vez que o usuário digita
searchInput.addEventListener('input', function() {
    const searchText = searchInput.value.toLowerCase();

    // Loop por todos os itens da lista e exibe ou esconde com base no que foi digitado
    items.forEach(function(item) {
        if (item.textContent.toLowerCase().includes(searchText)) {
            item.classList.remove('hidden');
        } else {
            item.classList.add('hidden');
        }
    });
});

/*transição do painel de cursos*/

function changeDescription(title, description) {
    // Get the elements where the title and description will be updated
    const dynamicTitle = document.getElementById('dynamic-title');
    const dynamicDescription = document.getElementById('dynamic-description');
    
    // Update the text content with a smooth transition
    dynamicTitle.style.opacity = 0;
    dynamicDescription.style.opacity = 0;
    
    setTimeout(() => {
        dynamicTitle.textContent = title;
        dynamicDescription.textContent = description;
        dynamicTitle.style.opacity = 1;
        dynamicDescription.style.opacity = 1;
    }, 300); // Delay to match the opacity transition
}


