__author__ = 'Vale Tolpegin & Matthew Nguyen'

# This program is the main brain of JARVIS
# This is extended into submodules in the following ways:
#   1: Submodules handle all post-parsing after appropriate module has been called
#   2: Functionality is increased by increasing JARVIS's capabilities

import sys
import subprocess
import os
import json

from core import *


class Brain:
    global user_gone


    def __init__( self, *args, **kwargs ):
        # Getting global variables
        global user_gone

        # Setting values of global variables
        user_gone = False


    def train( self, training_data ):
        """ This method will train jarvis using given training data """

        storage_adapter = JSONStorageAdapter()

        storage_adapter.train( training_data )


    def test_incoming_command( self, command ):
        # Getting global variables
        global user_gone

        # If the user was previously gone, but has started the conversation back up, greet him/her
        # TODO: convert hardcoded greeting to something more dynamic
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
        #try:
        # Getting context from database
        storage_adapter = JSONStorageAdapter()
        context = storage_adapter.get_database()
        self.hold_conversation( "", context )

        return
        """except:
            if self.handle_extensions( command ):
                return"""

        # Otherwise, since the command is not recognized, add it to the list of recognzed command
        print "Sorry sir, but I am still learning. I will save this phrase and learn it as time goes on. Is there a specific response you would like me to reply with?"
        save_phrase = raw_input( "COMMAND: " )
        if save_phrase != 'no':
            storage_adapter = JSONStorageAdapter()
            storage_adapter.add_information( [command, save_phrase] )

            # Telling the user the phrase has been saved
            print "The phrase has been saved"


    # This method will handle processing of the incoming command through modules
    def handle_extensions( self, phrase ):
        name_test = NameIdentifier()

        if name_test.test( phrase ):
            return True

        return True


    def hold_conversation( self, topic, previous_communication ):
        """ This is a recursive method to hold a conversation given a single topic """

        command = raw_input( "COMMAND: " )

        if self.handle_extensions( command ):
            response_generator = ResponseGenerator()
            similarity_tester = SimilarityMatch()

            response = response_generator.generate_response( command, previous_communication )

            storage_adapter = JSONStorageAdapter()
            storage_adapter.add_information( [ [ command, response ] ] )

            if similarity_tester.compare_topics( command, topic ):
                previous_communication.append( [command, response] )
                self.hold_conversation( topic, previous_communication )


# If this is run as a standalone program, tell the user that it is not meant to be that way
if __name__ == '__main__':
    print ""
    print "THIS IS NOT MEANT TO BE RUN AS A STANDALONE PROGRAM...PLEASE RUN 'python jarvis.py' to run JARVIS"
    print ""
