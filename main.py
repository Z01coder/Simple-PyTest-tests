def count_vowels(s):
    vowels = 'aeiouyAEIOUYаеёиоуыэюАЕЁИОУЫЭЮЯ'
    return sum(char in vowels for char in s.lower())