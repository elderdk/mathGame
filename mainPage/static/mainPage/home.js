let answerBox = document.querySelectorAll(".answer")
let score = 0;

answerBox.forEach(e => {
    e.addEventListener("keydown", event => {

        const currentRow = document.activeElement.className.split(' ')[1].split('r')[1];
        const correctAnswer = document.activeElement.parentElement.nextSibling.nextSibling.innerText.trim();
        const nextRowInput = document.querySelector(`.answer.r${Number(currentRow) + 1}`);
        const nextTR = document.activeElement.parentElement.parentElement.nextElementSibling;
        const currentTR = document.activeElement.parentElement.parentElement;
        const scoreBoard = document.querySelector("#scoreBoard");
        const raspberry = "<img src='/media/raspberry.png' class='rasp'>"
        const successSound = document.querySelector('#successSound')
        const scoreNumber = document.querySelector('#scoreNumber')

        if(event.keyCode === 13){
            if(e.value === correctAnswer){
                score++;
                scoreNumber.innerHTML = score;
                scoreBoard.innerHTML += raspberry;    // Add a raspberry if answer is correct
                successSound.play();
            }

            try {
                nextTR.style.display = "block";      // Show next tr
                currentTR.style.display = "none";    // hide current tr
                nextRowInput.focus()                 // focus on next tr's input    
            } catch (error) {
                setTimeout(location.reload(), 2000)  // instead of reloading automatically, it should display a "next" button, focused
            }
            
        };
    });
});

// event listener for exit settings button
exitSettingsButton = document.querySelector('#exitSettings')
settingsPage = document.querySelector('#settingsPage')

exitSettingsButton.addEventListener("click", event => {
    settingsPage.style.display = 'none';
})

// event listener for submit button to exit setting once clicked
submitButton = document.querySelector('button[type="submit"]')
submitButton.addEventListener("click", event => {
    settingsPage.style.display = 'none';
})

// event listener for settings open button
settingsOpenButton = document.querySelector('#settingsOpenButton')
settingsOpenButton.addEventListener("click", event => {
    settingsPage.style.display = 'block';
})