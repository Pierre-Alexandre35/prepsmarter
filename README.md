# test_prep


- How to display questions on users page? random? Need to keep track of the questions already answered



            {% for row in answers_data %}
            <ul id="question-options">
                <li class="question-answer" onclick='checkAnswer(
                    this, 
                    "A", 
                    `{{row[6]}}`,
                    `{{question_data[0][0]}}`,
                    )'>{{row[2]}}</li>
             <li class="question-answer" onclick='checkAnswer(
                this, 
                "B", 
                `{{row[6]}}`,
                `{{question_data[0][0]}}`,
                )'>{{row[3]}}</li>
             <li class="question-answer" onclick='checkAnswer(
                this, 
                "C", 
                `{{row[6]}}`,
                `{{question_data[0][0]}}`,
                )'>{{row[4]}}</li>
            </ul>
            {% endfor %}