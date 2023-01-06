# -*- coding: utf-8 -*-

"""
Text class.
"""

from textarium.utils import pipeline
import textarium.preprocessing as tp

class Text:
    def __init__(self, text: str):
        self.raw_text = text
        self.prepared_text = None

    def prepare(self):
        """Prepares text for analysis and ML modeling:
            - Removes punctuation, digits and extra spaces
            - Removes stopwords, html-tags and urls
            - Lemmatizes all words

        Returns:
            str: A prepared string
        """
        text = self.raw_text
        text = pipeline(text, 
            [
                tp.remove_html,
                tp.remove_urls,
                tp.remove_digits,
                tp.make_lowercase,
                tp.remove_punctuation
            ]
        )
        self.prepared_text = text

