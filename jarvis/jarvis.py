from brain import Brain


class JARVIS:

    def __init__(self, *args, **kwargs):
        self.jarvis_brain = Brain()

    def process(self, user_input):
        """
        Returns the response generated from the passed user_input variable
        """
        return self.jarvis_brain.generate_response(user_input)
