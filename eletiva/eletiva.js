document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.card-toggle').forEach(function (card) {
        card.addEventListener('click', function () {
            const target = card.getAttribute('data-target');
            const collapseElement = document.querySelector(target);
            if (collapseElement.classList.contains('collapse')) {
                collapseElement.classList.remove('collapse');
            } else {
                collapseElement.classList.add('collapse');
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const eletivasSection = document.getElementById('eletivas');

    // Função para aplicar fade-in ao carregar a página
    function fadeInOnLoad() {
        eletivasSection.classList.add('fade-in');
    }

    // Função para aplicar fade-out ao rolar a página
    function fadeOutOnScroll() {
        const scrollPosition = window.scrollY;
        if (scrollPosition > 100) {  // Ajuste a posição conforme necessário
            eletivasSection.classList.add('fade-out');
            eletivasSection.classList.remove('fade-in');
        } else {
            eletivasSection.classList.add('fade-in');
            eletivasSection.classList.remove('fade-out');
        }
    }

    // Aplicar fade-in ao carregar a página
    fadeInOnLoad();

    // Adicionar evento de scroll para fade-out
    window.addEventListener('scroll', fadeOutOnScroll);
});

