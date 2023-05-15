class Customerfeedback:
    def __init__(self, id, name, phone_number, email):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.feedback = None

    def give_feedback(self, text):
        self.feedback = text

