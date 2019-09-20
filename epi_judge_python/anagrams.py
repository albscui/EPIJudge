from test_framework import generic_test, test_utils


def find_anagrams(dictionary):
    anagram_map = {}
    for word in dictionary:
        group = anagram_map.setdefault(''.join(sorted(word)), [])
        group.append(word)

    return [group for group in anagram_map.values() if len(group) >= 2]


def find_anagrams_lower_case(dictionary):
    # convert counts of a word to a unique string and store in a hash table
    return


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
