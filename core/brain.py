""" Main brain for JARVIS """

from commandidentifier import CommandIdentifier
from chatbot import JarvisChatBot
from context_engine import *


class brain:
    global command_commander
    global contextengine
    global chatter_bot
    global conversation

    def __init__( self ):
        """ Blank constructor method """

        global command_commander
        global contextengine
        global chatter_bot
        global conversation

        command_commander = CommandIdentifier()
        contextengine = ContextEngine()
        chatter_bot = JarvisChatBot()
        conversation = []


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

        global command_commander
        global contextengine
        global chatter_bot
        global conversation

        # If the conversation is multiple pieces of dialog long
        if command_commander.use_previous_context():
            # Generate a response from the most suited command
            response, is_used = command_commander.select_command( user_input, conversation, contextengine.identify_important_information( user_input ) )

            # If that response is valid and should be displayed
            if is_used:
                # Updating conversation
                conversation.append( [ user_input, response ] )

                # Return the generated response
                return response
            else:
                # Updating conversation
                conversation = []

                # Otherwise, return a chat response
                return chatter_bot.generate_response( user_input )
        else:
            if ( contextengine.categorize( user_input ) == "command" or contextengine.categorize( user_input ) == "question" ):
                response, is_used = command_commander.select_command( user_input, conversation, contextengine.identify_important_information( user_input ) )

                if is_used:
                    return response
                else:
                    return chatter_bot.generate_response( user_input )
            elif ( contextengine.categorize( user_input ) == "chat" ):
                return chatter_bot.generate_response( user_input )
