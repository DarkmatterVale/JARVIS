__author__ = 'Vale Tolpegin & Matthew Nguyen'

"""

ResponseGenerator generates a response given previous context, the command/statement that needs a response, and trained data.

Class information:
- Version 0.0.1
- Stable: Yes
- In-use: Yes

"""

class ResponseGenerator:

    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass

    def generate_response( self, command, previous_communication ):
        """ This method generates the response that JARVIS will give to the given command """

        closest_match = []
        # Find closest match
        for communication in previous_communication:
            past_words = communication[ 0 ].split( ' ' )

            current_words = command.split( ' ' )

            if len( list(set( current_words ) - set( past_words )) ) / ( len( current_words ) + 0.0 ) < 0.4:
                closest_match = communication

                break

        # Compare closest match to its response -> generate new response based on new command and previous response
        general_response = []

        response_words = closest_match[ 1 ].split( ' ' )
        for response_word_index in range( 0, len( closest_match[ 1 ].split( ' ' ) ) ):
            if response_words[ response_word_index ] == closest_match[ 0 ].split( ' ' )[ response_word_index ]:
                general_response.append( response_word_index )
            else:
                general_response.append( str( response_words[ response_word_index ] ) )

        response = ""
        for individual_general_response in general_response:
            if type( individual_general_response ) is int:
                response += command.split( ' ' )[ individual_general_response ] + " "
            else:
                response += individual_general_response

        # Displaying what JARVIS will respond with
        print response

        # returning the response
        return response
