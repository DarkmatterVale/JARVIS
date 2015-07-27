__author__ = 'Vale Tolpegin & Matthew Nguyen'

"""

ResponseGenerator generates a response given previous context, the command/statement that needs a response, and trained data.

Class information:
- Version 0.0.1
- Stable: Yes
- In-use: Yes

"""

from JSONStorageAdapter import JSONStorageAdapter


class ResponseGenerator:

    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass


    def test_for_response( self, command ):
        """ This method tests to see whether the given command already has a response in the JSON database """

        storage_adapter = JSONStorageAdapter()
        database = storage_adapter.get_database()

        for entry in database:
            if entry[ 0 ] == command:
                return True, entry[ 1 ]

        return False, ""


    def generate_response( self, command, previous_communication ):
        """ This method generates the response that JARVIS will give to the given command """

        in_database, response = self.test_for_response( command )
        if in_database:
            print str( response )

            return response

        closest_match = [ [], 1 ]
        # Find closest match
        for communication in previous_communication:
            past_words = communication[ 0 ].split( ' ' )

            current_words = command.split( ' ' )

            if len( list(set( current_words ) - set( past_words )) ) / ( len( current_words ) + 0.0 ) < 0.5:
                if len( list(set( current_words ) - set( past_words )) ) / ( len( current_words ) + 0.0 ) < closest_match[ 1 ]:
                    closest_match = [ communication, len( list(set( current_words ) - set( past_words )) ) / ( len( current_words ) + 0.0 ) ]

        if closest_match == [ [], 1 ]:
            print "Hmm....I'm a little confused. What should I respond with?"

            response = str( raw_input( "COMMAND: " ) )
            return response

        # Compare closest match to its response -> generate new response based on new command and previous response
        general_response = []

        response_words = closest_match[ 0 ][ 1 ].split( ' ' )
        for response_word_index in range( 0, len( closest_match[ 0 ][ 1 ].split( ' ' ) ) ):
            if response_words[ response_word_index ] == closest_match[ 0 ][ 0 ].split( ' ' )[ response_word_index ]:
                general_response.append( response_word_index )
            else:
                general_response.append( str( response_words[ response_word_index ] ) )

        response = ""
        for individual_general_response in general_response:
            if type( individual_general_response ) is int:
                response += command.split( ' ' )[ individual_general_response ] + " "
            else:
                response += individual_general_response + " "

        # Displaying what JARVIS will respond with
        print response

        # returning the response
        return response
