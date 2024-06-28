# Find the longest sequence of zeros in a sequence of numbers.
# Return the length,  beginning (including) and the end (including) of that sequence in a list.
# For example, for the sequence [1, 2, 0, 0, 0, 3, 4, 0, 0, 0, 0, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 9]
# the result should be [6, 8, 13].


def longest_sequence(seq):
    longest = 0
    current = 0
    start = 0
    end = 0
    for i in range(len(seq)):
        if seq[i] == 0:
            current += 1
            if current > longest:
                longest = current
                start = i - longest + 1
                end = i
        else:
            current = 0
    return [longest, start, end]
