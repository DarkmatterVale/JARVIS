__author__ = 'Vale Tolpegin & Matthew Nguyen'

"""

SimilarityMatch compares to statements together and returns a value between 0 and 1 in addition to some other important information about the two statements

Class information:
- Version: 0.0.1
- Stable: Yes
- In-use: Yes

"""

class SimilarityMatch:

    def __init_( self, *args, **kwargs ):
        """ Blank constructor method """

        pass


    def compare_topics( self, command, topic ):
        """ This function compares statement_1 to statement_2. This entails using a number of different libraries and methods """

        if "Let's talk about something else" in command:
            return False
            #return 0, []

        #return 1, []
        return True
