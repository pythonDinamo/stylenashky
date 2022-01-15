let headerburger = document.querySelector('.header__burger');
    headerburger.addEventListener('click', showMenu);

function showMenu(){
    let menuNav = document.querySelector('.header__menu');

    headerburger.classList.toggle('active');
    menuNav.classList.toggle('active');
}