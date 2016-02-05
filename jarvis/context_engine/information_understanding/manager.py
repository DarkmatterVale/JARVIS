from sentence_structure import StructureIdentifier


class Manager:
    """
    Manager does exactly as its title suggests; it manages! Many different
    tools and methods are used to extract data, so this class compiles them
    all to gather the most important information within a text successfully.
    """

    def __init__(self):
        pass

    def return_important_info(self, user_input):
        """
        Returns all of the important information pertaining to the incoming
        text
        """
        # Getting all of the important information
        input_structure = self.get_input_structure(user_input)

        # Returning that information in the form of an array
        return [input_structure]

    def get_input_structure(self, user_input):
        """
        Returns the structure of the input. This is
        separated by sentences, like in the following
        example:

        { "This is the first test sentence" :
            { "prepositional_phrases" : "", "subject" : "This", "verb" : "is", "object" : "sentence", "object_descriptors" : "first test" }
        }
        """
        # Instantiating a structure identifier object
        jarvis_input_structure_identifier = StructureIdentifier()

        # Returning the structure of the input text
        return jarvis_input_structure_identifier.identify_structure(user_input)
