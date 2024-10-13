// Inicializar a SPA com a página inicial
window.addEventListener('load', () => {
    initializeComponents();
})

// Inicializa os componentes após o conteúdo da página ser carregado
function initializeComponents() {
    if (document.querySelector('.drawing-container')) {
        loadDrawingImages('drawing-container');
    }
    loadFlickity();
    initializeProfileNavigation();
}

// Função para trocar a página ao clicar nos links da navbar
function navigate(page, element) {
    loadPage(page);
    updateActiveLink(element);
}

// Atualiza o link ativo na navbar
function updateActiveLink(element) {
    const links = document.querySelectorAll('.navbar-nav .nav-link');
    links.forEach(link => link.classList.remove('active'));
    element.classList.add('active');
}


function form() {
    const formSection = document.getElementById("form-section");
    
    if (formSection.style.display === "none") {
        formSection.style.display = "block";
        formSection.style.opacity = 0;
        setTimeout(() => {
            formSection.style.opacity = 1;
            formSection.style.transition = "opacity 0.5s ease";
        }, 0);
    } else {
        formSection.style.opacity = 0;
        setTimeout(() => {
            formSection.style.display = "none";
        }, 500); // Tempo deve ser igual ao da transição
    }
}


