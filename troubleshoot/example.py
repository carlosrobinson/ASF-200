results= {
"response_code": 0,
"results": [
{
"category": "Geography",
"type": "multiple",
"difficulty": "easy",
"question": "What is the name of New Zealand&#039;s indigenous people?",
"correct_answer": "Maori",
"incorrect_answers": [
"Vikings",
"Polynesians",
"Samoans"
]
}
]
}

class Example:
    def __init__(self, question, correct_answer, incorrect_answers):
        self.correct_answer=correct_answer
        self.incorrect_answers=incorrect_answers


    def getcorrectAnswer(self):
        return self.correct_answer



    def getIncorrectAnswers(self):
        return self.incorrect_answers





class TriviaGame:
    def __init__(self):
        self.trivia_questions=[]
        
    
    
    
    def addQuestions(self, results):
        self.trivia_questions.append(results)


    def getAllQuestions(self):
        print(self.trivia_questions)
        return self.trivia_questions