class Question:
    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer


if __name__ == "__main__":
    q1 = Question("5+4=9?", "true")
    print(q1.text)
    print(q1.answer)
