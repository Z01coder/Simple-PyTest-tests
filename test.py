import pytest
from main import count_vowels

@pytest.mark.parametrize("input_string, expected_count", [
    ("аеиоуыэюАЭИОУЫЭЮ", 16),
    ("бвгджзклмнпрстфхцчшщъьБВГДЖЗКЛМНПРСТФХЦЧШЩЪЬ", 0),
    ("Привет! Как дела?", 5),
    ("aeiouyAEIOUY", 12),
    ("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ", 0),
    ("The quick brown fOx jumps over the lAzy dog", 12),
])
def test_count_vowels(input_string, expected_count):
    assert count_vowels(input_string) == expected_count