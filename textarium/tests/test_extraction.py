from unittest import TestCase

import textarium.extraction as extraction
from textarium.models import word_tokenizer

class TestExtraction(TestCase):
    def test_extract_tokens(self):
        test_input = "This line has 5 tokens"
        expected_result = ["This", "line", "has", "5", "tokens"]
        result = extraction.extract_tokens(test_input, tokenizer=word_tokenizer)
        self.assertEqual(expected_result, result)
