import datetime
from datetime import time


class Time:
    """
    Allows the user to get the current time
    """

    def __init__(self):
        pass

    def get_keywords(self):
        """
        Returns the words that specify this command being called
        """
        return ["time"]

    def should_respond(self, command, conversation, information):
        """
        Determines whether the incoming statement should be answered using
        this command module
        """
        # @TODO: Implement proper answer logic here
        return False

    def respond(self, command, conversation, information):
        """
        Returns the time the user asked for
        """
        for word_index in range(0, len(information[0]["pos_sentence"])):
            if "in" in information[0]["pos_sentence"][word_index]:
                if "second" in information[0]["pos_sentence"][word_index + 2][0]:
                    return "It will be " + self.addSecs(datetime.datetime.now().time(), int(information[0]["pos_sentence"][word_index + 1][0])), False
                elif "minute" in information[0]["pos_sentence"][word_index + 2][0]:
                    return "It will be " + self.addSecs(datetime.datetime.now().time(), 60 * int(information[0]["pos_sentence"][word_index + 1][0])), False
                elif "hour" in information[0]["pos_sentence"][word_index + 2][0]:
                    return "It will be " + self.addSecs(datetime.datetime.now().time(), 3600 * int(information[0]["pos_sentence"][word_index + 1][0])), False

        return "It is currently " + datetime.datetime.now().strftime("%H:%M:%S"), False

    def addSecs(self, tm, secs):
        """
        Adds a certain number of seconds on to the clock. This lets JARVIS
        predict the time in the future.
        """
        fulldate = datetime.datetime(1900, 1, 1, tm.hour, tm.minute, tm.second)
        fulldate = fulldate + datetime.timedelta(seconds=secs)

        return fulldate.strftime("%H:%M:%S")
