"""
Command module to give JARVIS the ability to run [Python] code

Module information:
- Author: Vale Tolpegin
- Version: 0.0.0

"""

class RunPrograms:

    def __init__( self ):
        """ Blank constructor method """

        pass


    def get_keywords( self ):
        """ Returns the words that specify this command is being run """

        return [ "run", "program" ]


    def run_code( self, user_input ):
        """ Runs the code the user would like to be run """

        return "Running the code now..."
