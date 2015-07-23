__author__ = 'Vale Tolpegin & Matthew Nguyen'

"""

This class will identify the following patterns in strings:

- Determining when someone is speaking to JARVIS

Class information:
- Version: 0.0.1
- Stable: Yes
- In-use: No

"""

class NameIdentifier:


    def __init__( self, command ):
        """
        Initializer method that processes incoming command to see if someone is talking to JARVIS.

        Output:
            --True: JARVIS is being spoken to
            --False: JARVIS is NOT being spoken to
        """

        return self.process( command )


    def process( self, command ):
        """ Looks for JARVIS' name in the command """

        if "JARVIS" in command:
            return True

        return False
