__author__ = 'Vale Tolpegin & Matthew Nguyen'

"""

ResponseGenerator generates a response given previous context, the command/statement that needs a response, and trained data.

Class information:
- Version 0.0.1
- Stable: Yes
- In-use: Yes

"""

from JSONStorageAdapter import JSONStorageAdapter
from regex4dummies import regex4dummies
from regex4dummies import Toolkit
import json


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
            print "I don't know what to say. What should I respond with?"
            response = str( raw_input( "COMMAND: " ) )

            print response

            return response
        elif type( closest_match[ 0 ] ) != type( "string" ):
            print "I don't know what to say. What should I respond with?"
            response = str( raw_input( "COMMAND: " ) )

            print response

            return response

        if len( closest_match[ 0 ][ 0 ].split( ' ' ) ) - len( command.split( ' ' ) ) < 2 and len( closest_match[ 0 ][ 0 ].split( ' ' ) ) - len( command.split( ' ' ) ) > -2:
            # Compare closest match to its response -> generate new response based on new command and previous response
            general_response = []

            response_words = closest_match[ 0 ][ 1 ].split( ' ' )
            for response_word_index in range( 0, len( closest_match[ 0 ][ 1 ].split( ' ' ) ) ):
                #print closest_match[ 0 ][ 0 ].split( ' ' )[ response_word_index ]
                if response_words[ response_word_index ] != '':
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


    def get_rules( self ):
        """ Get the contextual rules applied to text """

        try:
            database = json.load( open( 'learning/rules.json' ) )

            return database
        except:
            return {}


    def get_information( self, text ):
        """ Returns the dependencies and tokenized text """

        tool_kit = Toolkit()

        return [ tool_kit.tokenize( text, "pattern" ), tool_kit.find_dependencies( text, "pattern" ) ]


    def test_understood_context( self, new_text, previous_communication ):
        """ Tests to determine what to use to include in context """

        rules = self.get_rules()
        new_information = self.get_information( new_text )

        for rule in rules:
            pass

        return new_information
