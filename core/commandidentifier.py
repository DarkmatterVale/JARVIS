from command_modules import *

class CommandIdentifier:

    def __init__( self ):
        """ Blank constructor method """

        # Add custom commands to the following array
        self.commands = [
            Time()
        ]


    def select_command( self, user_input, conversation, command_information ):
        """ Determine which command should be executed & execute that command """

        # Determine whether previous context needs to be applied
        # The user_input must be related to a past question, not a new question that uses the same module
        for command in self.commands:
            if command.should_respond( user_input, conversation, command_information ):
                response, self.apply_previous_context = command.respond( user_input, conversation, command_information )

                return response, True

        # See if a module should be called on a new request
        selected_command_keywords = 0
        selected_command_index = 0

        for command_index in range( 0, len( self.commands ) ):
            keywords = self.commands[ command_index ].get_keywords()
            tested_command_keywords = 0

            for keyword in keywords:
                if keyword in user_input:
                    tested_command_keywords += 1

            if tested_command_keywords > selected_command_keywords:
                selected_command_keywords = tested_command_keywords
                selected_commnad_index = command_index

        if selected_command_keywords == 0:
            return "", False
        else:
            response, self.apply_previous_context = self.commands[ selected_command_index ].respond( user_input, conversation, command_information )
            self.previous_context_index = selected_command_index

            return response, True
