// Função para alternar entre as abas
function showTab(event, tabId) {
    // Esconder todas as abas
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(tab => tab.style.display = 'none');

    // Remover classe "active" dos links
    const tabLinks = document.querySelectorAll('.tab-link');
    tabLinks.forEach(link => link.classList.remove('active'));

    // Mostrar a aba selecionada e adicionar classe "active"
    document.getElementById(tabId).style.display = 'block';
    event.currentTarget.classList.add('active');
}
