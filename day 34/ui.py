from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="Score: 0",font=("Arial",10), fg="white", bg=THEME_COLOR)
        self.label.grid(row = 0, column=1)

        self.canvas = Canvas( width=300,height=250, bg="white")
        self.quiz_question = self.canvas.create_text(
            150,
            125,
            width=280, 
            text="title", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOR)
        self.canvas.grid(column = 0, row = 1, columnspan=2, pady=50)

        tick_image = PhotoImage(file="D:\\100P\\day 34\\quizzler-app-start\\images\\true.png")
        self.button_tick = Button(image=tick_image, highlightthickness=0, command= self.true_pressed)
        self.button_tick.grid(row=3, column=1)

        wrong_image = PhotoImage(file="D:\\100P\\day 34\\quizzler-app-start\\images\\false.png")
        self.button_wrong = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed)
        self.button_wrong.grid(row=3, column=0)

        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_question, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_question, text="You've reached end of the quiz")
            self.button_tick.config(state="disabled")
            self.button_wrong.config(state="disabled")
    
    def true_pressed(self):
        # is_right = self.quiz.check_answer("True")
        self.give_feedback(self.quiz.check_answer("True"))
    
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)