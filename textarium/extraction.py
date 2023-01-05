# -*- coding: utf-8 -*-

"""
Function for extracting information from texts.
"""

from typing import List
from razdel import sentenize
from nltk import tokenize

def extract_tokens(text: str, tokenizer) -> List[str]:
    """Extract tokens from a text

    Args:
        text (str): Any string
        tokenizer (_type_): A tokenizer object with a provided `.tokenize()` method

    Returns:
        List[str]: A list of extracted tokens
    """
    tokens = tokenizer.tokenize(text)
    return tokens

def extract_sentences(text: str, lang='en') -> List[str]:
    """Splits text string to a list of sentences

    Args:
        text (str): Any string in English or Russian
        lang (str): Text language ('ru' - Russian or 'en' - English)

    Returns:
        List[str]: A list of extracted sentences
    """
    if lang == 'en':
        sentences = tokenize.sent_tokenize(text)
    elif lang == 'ru':
        sentences = [i.text for i in sentenize(text)]
    return sentences

