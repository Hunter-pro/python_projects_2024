class QuizBrain:
    def __init__(self,ques_list):
        self.questions_list = ques_list
        self.question_num= 0
        self.score = 0
    
    def next_question(self):
        current_question = self.questions_list[self.question_num]
        self.question_num +=1
        user_ans = input(f"Q.{self.question_num} {current_question.text} (True/False): ")
        correct_ans = current_question.answer
        self.check_answer(user_ans,correct_ans)

    
    def still_have_questions(self):
        return self.question_num < len(self.questions_list)
    
    def check_answer(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score +=1
            print('You got it correct')
        else:
            print('sorry,you are wrong')
        print(f'the correct answer is : {correct_ans}')
        print(f" Your current score is {self.score}/{len(self.question_num)} \n")
        



    

