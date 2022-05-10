import requests
import random

class TriviaQuestion:
    """Randomly generated trivia questions"""
    def __init__(self, question, category,difficulty, correct_answer, incorrect_answers=[]):
        # self.id=id
        self.question=question
        self.category=category
        self.difficulty=difficulty
        self.correct_answer=correct_answer
        self.incorrect_answers=incorrect_answers


    


    def get_A_Question(self):
        return self.question



    def getCategory(self):
        return self.category




    def getDifficulty(self):
        return self.difficulty



    def getCorrectAnswer(self):
        return self.correct_answer



    def getIncorrectAnswers(self):
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



    # def getShuffledAnswers(self, retreived_questions):
    #     AllAnswers= []
    #     for challenge in retreived_questions['results']:
    #         for answer in challenge['incorrect_answers'] or answer in challenge['correect_answer']:
    #             AllAnswers.append(answer)

    #     random.shuffle(AllAnswers)
    #     print(AllAnswers)
    #     return AllAnswers








