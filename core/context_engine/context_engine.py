""" Main context engine class for JARVIS """


from input_categorizer import InputCategorizer
from information_understanding import *


class ContextEngine:
    global jarvis_information_gatherer

    def __init__( self ):
        """
        Constructor method
        """

        global jarvis_information_gatherer

        jarvis_information_gatherer = Manager()


    def categorize( self, user_input ):
        """ Returns the category of the user input """

        jarvis_input_categorizer = InputCategorizer()

        return jarvis_input_categorizer.categorize_input( user_input )


    def identify_important_information( self, user_input ):
        """
        Identifies the most important information found in the user input.

        This is very complicated. Because of this, all code related to this can be found in the subfolder information_understanding.
        """

        global jarvis_information_gatherer

        # Returning the important information related to the user input
        return jarvis_information_gatherer.return_important_info( user_input )
