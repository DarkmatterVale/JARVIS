"""
Class information:
- Author(s):
    - Vale Tolpegin
- Version: 1.0.0
"""


from regex4dummies import regex4dummies


class StructureIdentifier:
    global svo_triplet_identifier

    def __init__( self, *args, **kwargs ):
        """
        Constructor method
        """

        global svo_triplet_identifier

        svo_triplet_identifier = regex4dummies()


    def identify_structure( self, input ):
        """
        Returns the grammatical structure of the input
        """

        global svo_triplet_identifier

        # Identify the structure of the incoming text

        return {}
