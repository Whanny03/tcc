document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById('menu-icon');
    const menu = document.getElementById('menu');

    // Toggle the menu on icon click
    menuIcon.addEventListener('click', function(event) {
        menu.classList.toggle('show');
        event.stopPropagation();  // Prevents the menu from closing when clicking the icon
    });

    // Close the menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!menu.contains(event.target) && !menuIcon.contains(event.target)) {
            menu.classList.remove('show');
        }
    });
});

function showMenu(menuId) {
    // Hide all card sections
    const sections = document.querySelectorAll('.cardapio-secao');
    sections.forEach(function(section) {
        section.classList.add('oculto');
    });

    // Show the selected section
    const selectedSection = document.getElementById(menuId);
    selectedSection.classList.remove('oculto');
}

// Function to filter cards based on the selected shift
function filterMenu(turno) {
    var cards = document.querySelectorAll('.regularCards');

    cards.forEach(function(card) {
        // Hide all cards initially
        card.style.display = 'none';

        // Show only cards that belong to the selected shift
        if (card.classList.contains(turno)) {
            card.style.display = 'block';
        }
    });
}

// Add event listeners for filtering based on shift
document.querySelectorAll('#menu ul li a').forEach(function(link) {
    link.addEventListener('click', function(event) {
        event.preventDefault();
        const turno = event.target.getAttribute('onclick').split("'")[1]; // Extract turno value
        filterMenu(turno);
    });
});
