from test_framework import generic_test


def find_nearest_repetition(paragraph):
    d = {}
    ans = float("inf")
    for i, word in enumerate(paragraph):
        prev_i = d.get(word, None)
        if prev_i is not None:
            ans = min(ans, i-prev_i)
        d[word] = i
    return ans if ans != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
