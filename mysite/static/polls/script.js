document.getElementById('search-button').addEventListener('click', function() {
    const filterMenu = document.getElementById('filter-menu');
    filterMenu.classList.toggle('hidden');
});

// Применяем фильтры
document.getElementById('apply-filters').addEventListener('click', function() {
    const selectedBrands = Array.from(document.querySelectorAll('input[type="checkbox"]:checked'))
                                .map(checkbox => checkbox.value);
    alert('Выбранные бренды: ' + selectedBrands.join(', '));
    
   
});