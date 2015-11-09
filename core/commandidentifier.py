from command_modules import *

class CommandIdentifier:

    def __init__( self ):
        """ Blank constructor method """

        # Add custom commands to the following array
        self.commands = [
            Time()
        ]

        self.apply_previous_context = False
        self.previous_context_index = 0


    def use_previous_context( self ):
        """
        Returns whether the command needs more information
        and in turn the next input should be directed to that command
        """

        return self.apply_previous_context


    def select_command( self, user_input, conversation, command_information ):
        """ Determine which command should be executed & execute that command """

        # If a module is holding a conversation & needs to be called again
        if self.apply_previous_context:
            response, self.apply_previous_context = self.commands[ self.previous_context_index ].respond( user_input, conversation, command_information )

            return response, True
        else:
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
