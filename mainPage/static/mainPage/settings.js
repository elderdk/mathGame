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