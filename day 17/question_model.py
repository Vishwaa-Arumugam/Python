class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

new_ques = Question('','True')
print(new_ques.text)