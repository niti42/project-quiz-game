from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html


def decode_html_entities(text):
    """Decodes HTML entities like &#039; into their corresponding characters.

    Args:
        text: The string containing HTML entities.

    Returns:
        The string with decoded characters.
    """
    return html.unescape(text)


question_bank = []
for qa in question_data.get("results"):
    q = decode_html_entities(qa['question'])  # decode_html_entities()
    a = qa['correct_answer']
    question_bank.append(Question(q, a))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}")
