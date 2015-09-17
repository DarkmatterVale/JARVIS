""" Main context engine class for JARVIS """

from input_categorizer import InputCategorizer

class ContextEngine:

    def __init__( self ):
        """ Blank constructor method """

        pass


    def categorize( self, user_input ):
        """ Returns the category of the user input """

        jarvis_input_categorizer = InputCategorizer()

        return jarvis_input_categorizer.categorize_input( user_input )


    def identify_important_information( self, user_input ):
        """ Identifies the most important information found in the user input.

        This is very complicated. Because of this, all code related to this can be found in the subfolder information_gathering.
        """

        pass
