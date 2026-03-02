import pytest
from palindrome import longest_palindromic_substring

def test_simple_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"


def test_palindrome_in_middle():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]


def test_even_length_palindrome():
    assert longest_palindromic_substring("cbbd") == "bb"


def test_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_no_palindrome_longer_than_one():
    result = longest_palindromic_substring("abc")
    assert result in ["a", "b", "c"]

def test_long_string():
    long_string = "forgeeksskeegfor"
    assert longest_palindromic_substring(long_string) == "geeksskeeg"