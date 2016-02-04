from .base_case import JARVISTestCase


class JarvisTest(JARVISTestCase):

    def test_get_conversation(self):
        """
        Make sure that the get conversation method returns the
        conversation.
        """
        pass

class JarvisResponseTests(JARVISTestCase):

    def setUp(self):
        super(JarvisResponseTests, self).setUp()

        response_list = [
            Response("Hi")
        ]
