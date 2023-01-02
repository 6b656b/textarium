from unittest import TestCase

import textarium.preprocessing as preprocessing

class TestPreprocessing(TestCase):
    def test_remove_extra_spaces(self):
        test_input = " This line    has a lot of   extra spaces      "
        expected_result = "This line has a lot of extra spaces"
        result = preprocessing.remove_extra_spaces(test_input)
        self.assertEqual(expected_result, result)

    def test_remove_charset(self):
        test_input = "This 3line has0 !extra chars-"
        expected_result = "This line has extra chars"
        result = preprocessing.remove_charset(test_input, charset="30!-")
        self.assertEqual(expected_result, result)

    def test_remove_html(self):
        test_input = "<div>This line contains HTML-tags&nbsp</div>"
        expected_result = "This line contains HTML-tags"
        result = preprocessing.remove_html(test_input)
        self.assertEqual(expected_result, result)

    def test_remove_url(self):
        test_input = """
        This line contains URL http://google.com and 
        https://amazon.com https://yandex.ru/items?url=1
        """
        expected_result = "This line contains URL and"
        result = preprocessing.remove_urls(test_input)
        self.assertEqual(expected_result, result)