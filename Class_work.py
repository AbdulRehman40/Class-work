import streamlit as st

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer == self.correct_option

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        st.write(question.text)
        for i, option in enumerate(question.options, start=1):
            st.write(f"{i}. {option}")
        user_answer = st.number_input("Your answer (enter the number): ", min_value=1, max_value=len(question.options))
        return user_answer

    def run_quiz(self):
        for question in self.questions:
            user_answer = self.display_question(question)
            if question.is_correct(user_answer):
                st.success("Correct!")
                self.score += 1
            else:
                st.error(f"Wrong! The correct answer was {question.correct_option}: {question.options[question.correct_option - 1]}")
        st.write(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")

# Sample questions
questions = [
    Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3),
    Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 2),
    Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Dolphin"], 2),
]

# Create and run the quiz with Streamlit
def main():
    st.title("Simple Quiz Game with Streamlit")
    quiz = Quiz(questions)
    quiz.run_quiz()

if __name__ == "__main__":
    main()
