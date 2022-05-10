import requests, random,  triviaquestion
from random import shuffle



class TriviaGame(triviaquestion.TriviaQuestion):
    def __init__(self, question, category, difficulty, correct_answer, incorrect_answers=...):

        super().__init__(question, category, difficulty, correct_answer, incorrect_answers)
        self.questions=[]
        
    
    
    
    def addQuestions(self, results):
        self.questions.append(results)


    def getAllQuestions(self):
        return self.questions



    def getShuffledAnswers(self):
        # self.incorrect_answers=[]
        random.shuffle(self.incorrect_answers)
        return self.incorrect_answers




    def retrieveQuestions(self, catID, numQuestions):
        URL=f"https://opentdb.com/api.php?amount={numQuestions}&category={catID}&difficulty=medium&type=multiple"
        try:
            response=requests.get(URL, timeout=5)
            response.raise_for_status()
            response_JSON=response.json()
            return response_JSON
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)



    def saveAllQuestions(self, retrieved_questions):

        for challenge in retrieved_questions['results']:
            wrong_answer=[]
            # get answers
            for  answer in challenge['incorrect_answers']:
                wrong_answer.append(answer)
            founded_challenge=triviaquestion.TriviaQuestion(
                challenge["question"],
                challenge["category"],
                challenge["difficulty"],
                challenge["correct_answer"],
                challenge["incorrect_answers"]
            )
            self.questions.append(founded_challenge)

