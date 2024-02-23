from question_model import  Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    text = i["question"]
    ans = i["correct_answer"]
    new_question = Question(text,ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_have_questions():
    quiz.next_question()

print('You have completed the quiz')
print(f'you have score {quiz.score}/{len(quiz.question_num)}')


