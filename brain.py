__author__ = 'Vale Tolpegin & Matthew Nguyen'

import sys
import subprocess
import os
import json

# This program is the main brain of JARVIS
# This is extended into submodules in the following ways:
#   1: Submodules handle all post-parsing after appropriate module has been called
#   2: Functionality is increased

class brain:
    global user_gone

    def __init__( self, *args, **kwargs ):
        # Getting global variables
        global user_gone
        
        # Setting values of global variables
        user_gone = False

    def test_incoming_command( self, command ):
        # Getting global variables
        global user_gone
        
        # If the user was previously gone, but has started the conversation back up, greet him
        # TODO: convert hardcoded gretting to something more dynamic
        if user_gone:
            print "Hello again sir"
            user_gone = False
            return
        
        # Test for whether user wants to quit program...currently, this is hardcoded
        # TODO: convert hardcoded quit commands to dictionary synonyms of "no"
        if "quit" in command:
            exit(0)
        
        # If user-entered command is saying good bye to JARVIS, or the user wants JARVIS to "stop" paying attention to him
        # TODO: convert hardcoded commands into dictionary synonyms of "bye"
        if 'bye' in command or 'see ya later' in command:
            print "Ok, bye sir"
            user_gone = True
            
            return

        print "Sorry sir, but I am still learning. I will save this phrase and learn it as time goes on"

if __name__ == '__main__':
    print ""
    print "THIS IS NOT MEANT TO BE RUN AS A STANDALONE PROGRAM...PLEASE RUN 'python main.py' to run JARVIS"
    print ""
