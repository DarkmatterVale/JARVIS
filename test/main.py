""" Main JARVIS class """

from core import *


class jarvis:

    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass

    def run_jarvis( self ):
        """ Main method.....Interfaces with Jarvis' brain, gets commands and displays responses """

        jarvis_brain = brain()

        while True:
            user_input = raw_input( "Human: " )

            # Leave if the user is done
            if user_input == "quit":
                exit( 0 )

            # Generate response
            response = jarvis_brain.generate_response( user_input )

            # Print response
            print response


if __name__ == '__main__':
    jarvis_app = jarvis()

    jarvis_app.run_jarvis()
