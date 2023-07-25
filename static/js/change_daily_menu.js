        // Funkce pro načtení hodnot z buněk tabulky do formuláře
        function fillFormFromTable() {
            var volume = document.querySelector('.volume-cell').innerText.trim();
            var description = document.querySelector('.description-cell').innerText.trim();
            var allergens = document.querySelector('.allergens-cell').innerText.trim();
            var price = document.querySelector('.price-cell').innerText.trim();

            document.getElementById('volume').value = volume;
            document.getElementById('description').value = description;
            document.getElementById('allergens').value = allergens;
            document.getElementById('price').value = price;
        }

        // Předvyplnění formuláře hodnotami z tabulky po načtení stránky
        window.onload = function() {
            fillFormFromTable();
        };

        // Po odeslání formuláře aktualizovat obsah tabulky
        document.getElementById('editForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Zabránit výchozímu odeslání formuláře

            var volume = document.getElementById('volume').value;
            var description = document.getElementById('description').value;
            var allergens = document.getElementById('allergens').value;
            var price = document.getElementById('price').value;

            // Aktualizovat hodnoty v buněkách tabulky
            document.querySelector('.volume-cell').innerText = volume;
            document.querySelector('.description-cell').innerText = description;
            document.querySelector('.allergens-cell').innerText = allergens;
            document.querySelector('.price-cell').innerText = price;
        });