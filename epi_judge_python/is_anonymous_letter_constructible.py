from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    from collections import Counter

    letter_counts = Counter(letter_text)
    magazine_counts = Counter(magazine_text)

    for letter, count in letter_counts.items():
        if count > magazine_counts[letter]:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
