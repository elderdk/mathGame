// Parse the equation from home.html generated at views.py by main.py
const equations = JSON.parse(document.querySelector('#equation-list').textContent);
// Delete equation from the HTML element
document.querySelector('#equation-list').textContent = '';

// Generate TDs to fill in the TR
const createEquationTd = obj => {
    returnStr = '';
    obj.equation.forEach(e => {
        returnStr = returnStr + `<td class="equationNumber">${e}</td>`
    })
    returnStr = returnStr + '<td>=</td>'
    returnStr = returnStr + '<td><input type="number" class="answer"></td>'
    return returnStr
}

// Make new TR
const makeNewTr = n => {
    document.querySelector("#equation-tr").innerHTML = createEquationTd(equations[`${n}`])
}

// Fill in the equation-tr
let initialTR = 0;
makeNewTr(initialTR)

// Find answer box and set initial score
let answerBox = document.querySelector(".answer")
let score = 0;

// Autofocusing to the input box when the page is loaded
const doFocus = () => {
    document.querySelector("input[type='number']").focus()
    document.querySelector("input[type='number']").select()
}
doFocus()

// Set variables
const scoreBoard = document.querySelector("#scoreBoard");
const raspberry = "<img src='/media/raspberry.png' class='rasp'>"
const successSound = document.querySelector('#successSound')

// Increase score
const upScore = () => {
    score++;
    document.querySelector('#scoreNumber').innerHTML = score;
}

// Add event listener to the initial one and ones thereafter.
const refreshEventListener = ab => {
    ab.addEventListener("keydown", event => {
        const correctAnswer = equations[initialTR].answer;
    
        if(event.keyCode === 13){
            if(Number(answerBox.value) === correctAnswer){
                upScore();
                scoreBoard.innerHTML += raspberry;    // Add a raspberry if answer is correct
                successSound.play();
                initialTR++;

                // Try make new TR, reload the page if there's no more element in object
                try {
                    makeNewTr(initialTR)
                } catch(error) {
                    if(error instanceof TypeError){
                        setTimeout(() => {
                            location.reload();    
                        }, 300);
                    }
                }
                
                answerBox = document.querySelector(".answer")
                doFocus()
                return refreshEventListener(answerBox)
            }            
        };
    });   
}

// Run for the first time
refreshEventListener(answerBox)