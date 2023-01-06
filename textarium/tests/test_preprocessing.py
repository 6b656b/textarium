from unittest import TestCase

import textarium.preprocessing as preprocessing
from textarium.models import word_tokenizer

class TestPreprocessing(TestCase):
    def test_remove_extra_spaces_0(self):
        test_input = " This line    has a lot of   extra spaces      "
        expected_result = "This line has a lot of extra spaces"
        result = preprocessing.remove_extra_spaces(test_input)
        self.assertEqual(expected_result, result)

    def test_remove_charset_0(self):
        test_input = "This 3line has0 !extra chars-"
        expected_result = "This line has extra chars"
        result = preprocessing.remove_charset(test_input, charset="30!-")
        self.assertEqual(expected_result, result)

    def test_remove_html_0(self):
        test_input = "<div>This line contains HTML-tags&nbsp</div>"
        expected_result = "This line contains HTML-tags"
        result = preprocessing.remove_html(test_input)
        self.assertEqual(expected_result, result)

    def test_remove_url_0(self):
        test_input = """
        This line contains URL http://google.com and 
        https://amazon.com https://yandex.ru/items?url=1
        """
        expected_result = "This line contains URL and"
        result = preprocessing.remove_urls(test_input)
        self.assertEqual(expected_result, result)

    def test_remove_tokens_0(self):
        test_input = "This dog line contains cat extra mouse word bird tokens"
        tokens_to_exclude = ["dog", "cat", "mouse", "bird"]
        expected_result = "This line contains extra word tokens"
        result = preprocessing.remove_tokens(test_input, word_tokenizer, tokens_to_exclude)
        self.assertEqual(expected_result, result)

    def test_remove_digits_0(self):
        test_input = "This 3 line has 1234 random digits-10."
        expected_result = "This line has random digits- ."
        result = preprocessing.remove_digits(test_input)
        self.assertEqual(expected_result, result)

    def test_remove_punctuation_0(self):
        test_input = "Hello! I ne-ed remove, all : punctuation."
        expected_result = "Hello I ne ed remove all punctuation"
        result = preprocessing.remove_punctuation(test_input)
        self.assertEqual(expected_result, result)
