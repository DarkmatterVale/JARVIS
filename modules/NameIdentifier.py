__author__ = 'Vale Tolpegin & Matthew Nguyen'

"""

This class will identify the following patterns in strings:

- Determining when someone is speaking to JARVIS

Class information:
- Version: 0.0.1
- Stable: Yes
- In-use: Yes

"""

class NameIdentifier:


    def __init__( self ):
        """ Blank constructor method """

        pass


    def test( self, command ):
        """ Interface method to the process function """

        return self.process( command )


    def process( self, command ):
        """ Looks for JARVIS' name in the command """

        if "JARVIS" in command:
            return True

        return False
