class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First, check if lengths are the same
        if len(s) != len(t):
            return False

        # Sort and reassign the strings
        s = "".join(sorted(s))
        t = "".join(sorted(t))

        # Use a single index to compare characters
        i = 0
        while i < len(s):
            if s[i] != t[i]:  # Compare each character in sorted strings
                return False
            i += 1

        # If all characters matched, the strings are anagrams
        return True
