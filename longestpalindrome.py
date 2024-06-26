def longestPalindrome(s):
    c = 0  # odd count
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
        if freq[ch] % 2 == 0:
            c -= 1
        else:
            c += 1

    if c > 1:
        return len(s) - c + 1
    return len(s)