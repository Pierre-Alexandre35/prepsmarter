

function checkAnswer(divSelected, selectedAnswer, correctAnswer){
  console.log(correctAnswer)
  console.log(selectedAnswer)

  if(selectedAnswer == correctAnswer){
    divSelected.style.backgroundColor = "green";
  }
  else{
    divSelected.style.backgroundColor = "red";

  }
}