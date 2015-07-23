__author__ = 'Vale Tolpegin & Matthew Nguyen'

# This program is the main brain of JARVIS
# This is extended into submodules in the following ways:
#   1: Submodules handle all post-parsing after appropriate module has been called
#   2: Functionality is increased by increasing JARVIS's capabilities

import sys
import subprocess
import os
import json

sys.path.insert( 0, os.getcwd() + r"\\modules\\" )

from name_processor import NameIdentifier


class Brain:
    global user_gone


    def __init__( self, *args, **kwargs ):
        # Getting global variables
        global user_gone

        # Setting values of global variables
        user_gone = False


    def test_incoming_command( self, command ):
        # Getting global variables
        global user_gone

        # If the user was previously gone, but has started the conversation back up, greet him/her
        # TODO: convert hardcoded gretting to something more dynamic
        if user_gone:
            print "Hello again sir"

            user_gone = False
            return

        # Test for whether user wants to quit program...currently, this is hardcoded
        # TODO: convert hardcoded quit commands to dictionary synonyms of "quit"
        if "quit" in command:
            exit(0)

        # If user-entered command is saying good bye to JARVIS, or the user wants JARVIS to "stop" paying attention to him
        # TODO: convert hardcoded commands into dictionary synonyms of "bye"
        if 'bye' in command or 'see ya later' in command:
            print "Goodbye sir"

            user_gone = True
            return

        # Otherwise, a set resposne is going to be loaded. In the future, this will be removed and just handle_extensions() will be called.
        try:
            data = json.load( open( 'learning/phrase_list.json' ) )
            print data[ command ][ 'response' ]

            return
        except:
            if self.handle_extensions( command ):
                print "Hello Sir"
                return

        # Otherwise, since the command is not recognized, add it to the list of recognzed command
        print "Sorry sir, but I am still learning. I will save this phrase and learn it as time goes on. Is there a specific response you would like me to reply with?"
        save_phrase = raw_input( "COMMAND: " )
        if save_phrase != 'no':
            # Opening file, to read and then to write
            output = {}
            try:
                output = json.load( open( 'learning/phrase_list.json' ) )
            except:
                pass

            file = open( 'learning/phrase_list.json', 'w' )

            # Creating the entry for the file
            output[ command ] = { "response" : save_phrase }

            # Putting the entry in the file
            json.dump( output, file )

            # Closing the file since all I/O operations have been completed
            file.close()

            # Telling the user the phrase has been saved
            print "The phrase has been saved"


    # This method will handle processing of the incoming command through modules
    def handle_extensions( self, phrase ):
        name_test = NameIdentifier()

        return name_test.test()


# If this is run as a standalone program, tell the user that it is not meant to be that way
if __name__ == '__main__':
    print ""
    print "THIS IS NOT MEANT TO BE RUN AS A STANDALONE PROGRAM...PLEASE RUN 'python jarvis.py' to run JARVIS"
    print ""
