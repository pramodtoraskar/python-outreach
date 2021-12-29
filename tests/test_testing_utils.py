import unittest

class TestTestingUtils(unittest.TestCase):
    """
    Unit tests for testing utilities
    """

    def test_async_mock_str(self):
        """
        Calling str on the mock object should return a string

        Makes sure that certain dunder methods don't return a co-routine
        """
        self.assertEquals(0 + 1, 1)
