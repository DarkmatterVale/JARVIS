class jarvis:

    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass

    def run_jarvis( self ):
        """ Main method.....Interfaces with Jarvis' brain, gets commands and displays responses """

        while True:
            user_input = raw_input( "Human: " )

            # response = TODO: Interface to brain & generate a response

            # print response


if __name__ == '__main__':
    jarvis_app = jarvis()

    jarvis_app.run_jarvis()
