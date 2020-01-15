const choreBoxes = document.querySelectorAll('.choreBox')
const successSound = document.querySelector('#successSound')

// Add event listeners
choreBoxes.forEach(e => {
    e.addEventListener('click', event => {
        successSound.play();
    });
})