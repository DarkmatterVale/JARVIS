"""
Class information:
- Author(s):
    - Vale Tolpegin
- Version: 1.0.0
"""


from regex4dummies import Toolkit
import nltk


class StructureIdentifier:

    def __init__( self, *args, **kwargs ):
        """
        Constructor method
        """

        self.svo_triplet_identifier = Toolkit()


    def identify_structure( self, user_input ):
        """
        Returns the grammatical structure of the input
        """

        # Identify the structure of the incoming text
        svo_triplet = self.svo_triplet_identifier.find_dependencies( text=user_input, parser="pattern" )
        pos_sentence = nltk.pos_tag( nltk.word_tokenize( user_input ) )

        # Return the structure
        return { "pos_sentence" : pos_sentence,
                    "svo" : svo_triplet }
