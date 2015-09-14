""" Main brain for JARVIS """

from commandidentifier import CommandIdentifier
#from chatbot import ChatBot
from context_engine import *


class brain:
    global command_commander
    global contextengine

    def __init__( self ):
        """ Blank constructor method """

        global command_commander
        global contextengine

        command_commander = CommandIdentifier()
        contextengine = ContextEngine()


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

        if ( contextengine.categorize( user_input ) == "command" or contextengine.categorize( user_input ) == "question" ):
            return command_commander.select_command( user_input )
        elif ( contextengine.categorize( user_input ) == "chat" ):
            return "Whoops...Still learning how to talk to people....Come back soon for some more information!"
            #return command_commander.get_response( user_input )
