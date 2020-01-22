goldcoins = document.querySelectorAll('.goldcoin')

goldcoins.forEach(e => {
    // Difficult to use removeEventListener for anonymous handler hence the below method
    e.addEventListener("click", function handler() {
        addAjax();
        e.classList.add('coinspent')
        e.removeEventListener('click', handler)
    })
})