const menu = document.querySelector('.mobile-menu');
const NavMenu = document.querySelector('.nav-list');

menu.addEventListener('click', () => {
    menu.classList.toggle('ativo');
    NavMenu.classList.toggle('ativo');
})