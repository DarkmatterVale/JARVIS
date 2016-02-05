import nltk


class InputCategorizer:
    """
    Categorizes the user input to determine whether the user is:
    - Asking a question
    - Giving a command
    - Or just chatting
    """

    def __init__(self):
        self.ignore_words = [
            "JARVIS"
        ]

    def categorize_input(self, user_input):
        """
        Identify whether user input is either a command/question, or other
        """
        # Initializing a variable
        category = ""

        # Normalizing user input
        normalized_user_input = self.normalize_input(user_input)

        # Get the part of speech of the incoming user input. This assumes that the user only gives single sentence commands, questions, or chats
        pos_sentence = nltk.pos_tag(nltk.word_tokenize(str(normalized_user_input)))

        # Checking whether the first word in the sentence is a verb
        if "VB" in pos_sentence[0][1]:
            category = "command"
        elif "?" in user_input:
            category = "question"
        else:
            category = "chat"

        # Returning the identified category
        return category


    def normalize_input(self, text):
        """
        Normalizes the text so that unnecessary information is removed,
        grammar corrected, etc
        """
        # Removing words to ignore
        for word_to_ignore in self.ignore_words:
            for word_index in range(0, len(text.split(' '))):
                if word_to_ignore in text.split(' ')[word_index]:
                    text = ' '.join(text.split(' ')[: word_index]) + ' '.join(text.split(' ')[word_index + 1 :])

                    break

        # Returning normalized text
        return text
