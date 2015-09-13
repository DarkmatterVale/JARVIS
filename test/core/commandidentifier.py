from command_modules import *

class CommandIdentifier:
    global commands

    def __init__( self ):
        """ Blank constructor method """

        global commands

        commands = [
            Time()
        ]


    def select_command( self, user_input ):
        """ Determine which command should be executed & execute that command """

        global commands

        selected_command_keywords = 0
        selected_command_index = 0

        for command_index in range( 0, len( commands ) ):
            keywords = commands[ command_index ].get_keywords()
            tested_command_keywords = 0

            for keyword in keywords:
                if keyword in user_input:
                    tested_command_keywords += 1

            if tested_command_keywords > selected_command_keywords:
                selected_command_keywords = tested_command_keywords
                selected_commnad_index = command_index

        if selected_command_keywords == 0:
            return "Ummm...I don't know how to do that...Sorry"
        else:
            return commands[ selected_command_index ].respond( user_input, [] )
