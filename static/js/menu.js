    // Funkce pro zavírání/zobrazování menu po kliknutí na tlačítko
    function toggleMenuCollapse() {
        var menu = document.getElementById('mainMenu');
        var windowHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight || 0;
        var shouldCollapse = windowHeight < 680;

        if (shouldCollapse) {
            menu.classList.add('collapsed');
        } else {
            menu.classList.remove('collapsed');
        }
    }

    // Spuštění při načtení stránky a při změně velikosti okna
    window.addEventListener('DOMContentLoaded', toggleMenuCollapse);
    window.addEventListener('resize', toggleMenuCollapse);

    // Funkce pro otevírání/zavírání menu po kliknutí na tlačítko
    var navbarToggler = document.querySelector('.navbar-toggler');
    navbarToggler.addEventListener('click', function () {
        var menu = document.getElementById('mainMenu');
        menu.classList.toggle('show');
    });