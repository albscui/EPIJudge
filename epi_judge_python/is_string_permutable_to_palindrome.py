from test_framework import generic_test


def can_form_palindrome(s):
    from collections import Counter
    c = Counter(s)
    num_odds = 0
    for v in c.values():
        if v % 2 != 0:
            num_odds += 1
    return num_odds <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
