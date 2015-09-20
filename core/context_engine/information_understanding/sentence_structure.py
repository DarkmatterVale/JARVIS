"""
Class information:
- Author(s):
    - Vale Tolpegin
- Version: 1.0.0
"""


from regex4dummies import regex4dummies
import nltk


class StructureIdentifier:
    global svo_triplet_identifier

    def __init__( self, *args, **kwargs ):
        """
        Constructor method
        """

        global svo_triplet_identifier

        svo_triplet_identifier = regex4dummies()


    def identify_structure( self, user_input ):
        """
        Returns the grammatical structure of the input
        """

        global svo_triplet_identifier

        # Identify the structure of the incoming text
        #svo_triplets = svo_triplet_identifier.

        return { "pos_sentence" : nltk.pos_tag( nltk.word_tokenize( user_input ) ) }
