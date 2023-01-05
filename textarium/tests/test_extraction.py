from unittest import TestCase

import textarium.extraction as extraction
from textarium.models import word_tokenizer

class TestExtraction(TestCase):
    def test_extract_tokens(self):
        test_input = "This line has 5 tokens"
        expected_result = ["This", "line", "has", "5", "tokens"]
        result = extraction.extract_tokens(test_input, tokenizer=word_tokenizer)
        self.assertEqual(expected_result, result)

    def test_extract_sentences_en(self):
        text_input = """
        Hello! My name is Robbie. 
        Please, write an email to Mr. Parker. 
        His email: parker@gmail.com.
        """
        expected_result = [
            "Hello!", "My name is Robbie.", 
            "Please, write an email to Mr. Parker.", 
            "His email: parker@gmail.com."
        ]
        result = extraction.extract_sentences(text_input, lang='en')
        self.assertEqual(expected_result, result)