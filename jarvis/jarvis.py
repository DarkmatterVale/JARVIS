from brain import *


class JARVIS:

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        self.jarvis_brain = brain()

    def get_response(self, user_input):
        """
        Returns the response generated from the passed user_input variable
        """
        return self.jarvis_brain.generate_response(user_input)
