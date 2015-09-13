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

        return "It is currently " + datetime.datetime.now().strftime("%H:%M:%S")
