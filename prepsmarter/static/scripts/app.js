function storeAnwserStats(questionId, answerId){
    $.ajax({
      url : "/store_stats",
      type : "POST",
      data : JSON.stringify({
                question_id: questionId,
                answer_id:answerId, 
              }),
      contentType: 'application/json; charset=utf-8',
      dataType: 'json',
  })
  .done(function(data){
      console.log("After " +data["correct_answer"]);
  });
  }
  
  function checkAnswer(divSelected, answerId, questionId, isCorrect){
    already_answered = false
    if(isCorrect == 1){
      divSelected.style.backgroundColor = "green";
    }
    else{
      divSelected.style.backgroundColor = "red";
    }
    storeAnwserStats(questionId, answerId)
  }
  
  
  