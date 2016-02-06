from commandidentifier import CommandIdentifier
from chatbot import JarvisChatBot
from context_engine import *


class Brain:
    """
    Main brain for JARVIS
    """

    def __init__(self):
        self.command_commander = CommandIdentifier()
        self.contextengine = ContextEngine()
        self.chatter_bot = JarvisChatBot()
        self.conversation = []


    def generate_response(self, user_input):
        """
        Generates a response based on the incoming user command.

        Uses:
        - context engine
            - Categorize user input
        - command identifier
            - Determine which command should be executed
        - chatbot
            - Generate a correct response

        Outputs:
        - returns response
        """

        if (self.contextengine.categorize(user_input) == "command" or self.contextengine.categorize(user_input) == "question"):
            response, is_used = self.command_commander.select_command(user_input, self.conversation, self.contextengine.identify_important_information(user_input))

            if is_used:
                # Updating conversation
                self.conversation.append([user_input, response])

                return response
            else:
                # Updating conversation
                self.conversation.append([user_input, ""])

                return self.chatter_bot.generate_response(user_input)
        elif (self.contextengine.categorize(user_input) == "chat"):
            # Updating conversation
            self.conversation.append([user_input, ""])

            return self.chatter_bot.generate_response(user_input)
