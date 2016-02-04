from core import *


class Jarvis:
    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        self.jarvis_brain = brain()

    def run_jarvis(self):
        """
        Interfaces with Jarvis' brain and displays responses
        """
        while True:
            user_input = raw_input("Human: ")

            # Leave if the user is done
            if user_input == "quit":
                exit(0)

            # Generate response
            response = self.jarvis_brain.generate_response(user_input)

            # Print response
            print response


    def get_response(self, user_input):
        """
        Returns the response generated from the passed user_input variable
        """
        return self.jarvis_brain.generate_response( user_input )


if __name__ == '__main__':
    jarvis_app = Jarvis()

    jarvis_app.run_jarvis()
