# -*- coding: utf-8 -*-

"""
Text cleaning and preprocessing functions.
"""

import re
import string
import unicodedata
from typing import List, Set, Union


def remove_extra_spaces(text: str) -> str:
    """_summary_

    Args:
        text (str): My Description

    Returns:
        str: _description_
    """
    text_wo_extra_spaces = " ".join(text.split())

    return text_wo_extra_spaces.strip()

def remove_charset(text: str, charset: string) -> str:
    """_summary_

    Args:
        text (str): _description_
        charset (Set): _description_

    Returns:
        str: _description_
    """
    text_wo_charset = text.translate(
        str.maketrans(charset, " " * len(charset))
    )
    text_wo_charset = remove_extra_spaces(text_wo_charset)

    return text_wo_charset


