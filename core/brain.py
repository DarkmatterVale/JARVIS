""" Main brain for JARVIS """

from commandidentifier import CommandIdentifier
from chatbot import JarvisChatBot
from context_engine import *


class brain:

    def __init__( self ):
        """ Blank constructor method """

        self.command_commander = CommandIdentifier()
        self.contextengine = ContextEngine()
        self.chatter_bot = JarvisChatBot()
        self.conversation = []


    def generate_response( self, user_input ):
        """ Generates a response based on the incoming user command.

        Uses:
        - context engine
            - Categorize user input
        - command identifier
            - Determine which command should be executed
        - chatbot
            - Generate a correct response

        Outputs:
        - returns response"""

        # If the conversation is multiple pieces of dialog long
        if self.command_commander.use_previous_context():
            # Generate a response from the most suited command
            response, is_used = self.command_commander.select_command( user_input, self.conversation, self.contextengine.identify_important_information( user_input ) )

            # If that response is valid and should be displayed
            if is_used:
                # Updating conversation
                self.conversation.append( [ user_input, response ] )

                # Return the generated response
                return response
            else:
                # Updating conversation
                self.conversation = []

                # Otherwise, return a chat response
                return self.chatter_bot.generate_response( user_input )
        else:
            if ( self.contextengine.categorize( user_input ) == "command" or self.contextengine.categorize( user_input ) == "question" ):
                response, is_used = self.command_commander.select_command( user_input, self.conversation, self.contextengine.identify_important_information( user_input ) )

                if is_used:
                    return response
                else:
                    return self.chatter_bot.generate_response( user_input )
            elif ( self.contextengine.categorize( user_input ) == "chat" ):
                return self.chatter_bot.generate_response( user_input )
