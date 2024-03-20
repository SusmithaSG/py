import tkinter as tk
class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option
class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(master, text="",font=("helvetica",18),bg="light blue",fg="black")
        self.question_label.pack()

        self.radio_var = tk.IntVar()

        self.radio_buttons = []
        for i, option in enumerate(self.questions[self.current_question_index].options):
            radio_button = tk.Radiobutton(master, text=option, font=("helvetica",14),fg="black",variable=self.radio_var, value=i)
            radio_button.pack()
            self.radio_buttons.append(radio_button)

        submit_button = tk.Button(master, text="Submit",font=("ariel",14),bg="light grey",fg="black",command=self.check_answer)
        submit_button.pack()

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question.text)

            for i, option in enumerate(question.options):
                self.radio_buttons[i].config(text=option)

            self.radio_var.set(-1)  # Deselect all radio buttons

    def check_answer(self):
        selected_option = self.radio_var.get()

        if selected_option == self.questions[self.current_question_index].correct_option:
            self.score += 1

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.next_question()
        else:
            self.show_result()

    def show_result(self):
        result_text = f"You scored {self.score} out of {len(self.questions)}!"
        result_label = tk.Label(self.master, text=result_text,font=("Ariel",16),bg="violet",fg="black")
        result_label.pack()

if __name__ == "__main__":
    # Sample questions
    q1 = Question("What is the our National Animal?", ["Tiger","Elephant","Lion","Hippo"], 0)
    q2 = Question("What is the our National Bird?", ["Peacock","King Fisher","Eagle","Crow"], 0)
    q3 = Question("What is the largest Animal?", ["Dolphine", "Elephant", "Giraffe", "Hippopotamus"], 1)

    questions_list = [q1, q2, q3]

    root = tk.Tk()
    root.title("Simple Quiz App")
    root.geometry("400x400")

    app = QuizApp(root, questions_list)

    root.mainloop()
