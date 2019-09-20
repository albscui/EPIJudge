import heapq

from test_framework import generic_test


def online_median(sequence):
    max_heap, min_heap = [], []
    result = []
    for x in sequence:
        heapq.heappush(min_heap, -heapq.heappushpop(max_heap, -x))

        if len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        result.append(0.5 * (min_heap[0] + (-max_heap[0]))
                      if len(min_heap) == len(max_heap) else -max_heap[0])

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
