const submitButton = document.getElementById("submit");
const plusOuMoins = document.getElementById("plus-moins");
const essaisRestants = document.getElementById("essais-restants");
const guess = document.getElementById("guess");
const restartButton = document.getElementById("restart");
const boom = new Audio("./sons/boom.mp3");
const cMoins = new Audio("./sons/c_moins.mp3");
const cPlus = new Audio("./sons/c_plus.mp3");
const reset = new Audio("./sons/reset.mp3");
const select = new Audio("./sons/select.mp3");
const vic = new Audio("./sons/vic.mp3");
const triste = "url(\"https://media.tenor.com/lR6202nFryoAAAAC/billy-rebeudeter.gif\")"
const masterclass = "url(\"https://media.tenor.com/i6tZg1Nnd4cAAAAd/masterclass-masterclass-jacob.gif\")"
const commentCaMonBoeuf = "url(\"https://media.tenor.com/yj0ADLLcoCcAAAAC/quoi-comment-ca-mon-reuf.gif\")"

function getRandomNumber(max){
    return Math.floor(Math.random() * max);
}

let nombre = getRandomNumber(10000).toString();

function spawnRestart(){
    restartButton.style.display = "inline";
}

function moins(){
    plusOuMoins.innerText = "C'est moins!!!!";
    cMoins.play()
}
function plus(){
    plusOuMoins.innerText = "C'est plus!!!!";
    cPlus.play()
}
function gg(){
    plusOuMoins.innerText = "C'est gagné!!!!";
    vic.play()
    document.body.style.backgroundImage = masterclass;
    spawnRestart();
}
function loose(){
    plusOuMoins.innerText = "C'est perdu man!!!!";
    boom.play();
    document.body.style.backgroundImage = triste;
    spawnRestart();
}


submitButton.addEventListener('click', () => {
    select.play();
    essaisRestants.innerText -= 1;

    guessValue = guess.value;

    if(parseInt(essaisRestants.innerText) <= 0) {
        loose();
        return;
    }
    if(guessValue == nombre){
        gg();
    } else if(guessValue < nombre){
        plus();
    } else if(guessValue > nombre){
        moins();
    } else{
        alert(`ERREUR WHAT DSL LE NOMBRE C'ÉTAIT ${nombre} (essaie pour voir)`);
    }
    
})

restartButton.addEventListener('click', () => {
    reset.play()
    nombre = getRandomNumber(10000).toString();
    essaisRestants.innerText = "15";
    plusOuMoins.innerText = "";
    document.body.style.backgroundImage = commentCaMonBoeuf;
    restartButton.style.display = "none";
})