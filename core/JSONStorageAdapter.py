__author__ = 'Vale Tolpegin & Matthew Nguyen'

"""

JSONStorageAdapter allows JARVIS to interface with JSON files as storage for conversations, actions, etc.

Class Information:
- Version: 0.0.1
- Stable: Yes
- In-use: Yes

"""

import os
import json


class JSONStorageAdapter:

    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass


    def train( self, training_data ):
        """ This method trains JARVIS with a set of given commands and responses """

        for index in xrange( 0, len( training_data ) - 1, 2 ):
            self.add_information( [[training_data[ index ], training_data[ index + 1 ]]] )


    def get_database( self ):
        """ Returns the JSON database of commands """

        try:
            database = json.load( open( 'learning/phrase_list.json' ) )
        except:
            return {}

        database_list = []
        for entry in database:
            database_list.append( [entry, database[ entry ][ "response" ]] )

        return database_list


    def add_information( self, information ):
        """ This method will add the given information to the JSON file containing all command information """

        # Opening JSON file, to read and then to write
        output = {}
        try:
            output = json.load( open( 'learning/phrase_list.json' ) )
        except:
            pass

        file = open( 'learning/phrase_list.json', 'w' )

        if type( information ) is list:
            for item in information:
                # Creating the entry for the file
                output[ item[ 0 ] ] = { "response" : item[ 1 ] }
        else:
            # Creating the entry for the file
            output[ information[ 0 ] ] = { "response" : information[ 1 ] }

        # Putting the entry in the file
        json.dump( output, file )

        # Closing the file since all I/O operations have been completed
        file.close()
