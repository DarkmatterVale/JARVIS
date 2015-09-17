"""
This command module allows the user to get the current time.

Module information:
- Author: Vale Tolpegin
- Version: 1.0.0

"""

import datetime
from datetime import time


class Time:

    def __init__( self ):
        """ Blank constructor method """

        pass


    def get_keywords( self ):
        """ Returns the words that specify this command being called """

        return [ "time" ]


    def respond( self, command, information ):
        """ Returns the current time

        Outputs/System variable changes:
        - returns time"""

        # Below code is tentative...will be updated as soon as some work is done on the context engine
        if " in" in command:
            return "In how many minutes?", True
        elif " is" in command:
            return "It is currently " + datetime.datetime.now().strftime("%H:%M:%S"), False
        elif " minutes" in command or " minute" in command:
            return "It will be " + datetime.datetime.now().strftime("%H") + ":" + str( int( datetime.datetime.now().strftime("%M") ) + int( command.split( ' ' )[ 0 ] ) ) + ":" + datetime.datetime.now().strftime("%S"), False
